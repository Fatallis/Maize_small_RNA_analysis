#!/usr/bin/python
import argparse, HTSeq, gzip, os.path, itertools, sys

# Get the list of organisms and get abbreviations
def parse_species_list(organisms_file,filter_string,index):
	'''This function reads the organisms_file and returns
	a list of species abbreviations.'''

	def process_the_list(of,index):
		filtered_species=list()
		for line in of:
			line=line.split('\t')
			if filter_string in line[index]:
				filtered_species.append(line[0])
		return filtered_species

	# Open the organisms file zipped or unzipped.
	try:
		with gzip.open(organisms_file) as of:
			filtered_species=process_the_list(of,index)
	except:
	    with open(organisms_file) as of:
	        filtered_species=process_the_list(of,index)

	return filtered_species

# Search for the specie abbreviation in the	name of the fasta record and saved in a new file if belong to filtered_species.
def filter_file(all_miRNAs_file,filtered_species,filter_string):
	'''This funtion search for the specie abreviation in the
	name of the fasta record and if it is in the filtered_species
	the fasta record is saved in a new file.'''
	with open(output_file,'w') as out:
		for seq in HTSeq.FastaReader(all_miRNAs_file):
			specie=seq.name.split('-')[0]
			if specie in filtered_species:
				seq.write_to_fasta_file(out)

# Define the command-line interface
parser=argparse.ArgumentParser(description='This script filter the full fasta files from miRBase to a specific group of records containing the entered scientific name.')
parser.add_argument('organisms_file', help='Organisms file from miRBase.')
parser.add_argument('miRBase_fasta_file', help='Fasta file from miRBase (mature, hairpin).')
parser.add_argument('scientific_name', help='The records will be filtered in base of the scientific name. (e.g. "Zea mays", "Homo sapiens").')
parser.add_argument('-o', action='store_true', help='The search is carried on by organism key (e.g. "zma", "hsa").')
parser.add_argument('-t', action='store_true', help='The search is carried on by taxonomy term (e.g. "Viridiplantae", "Metazoa").')
parser.add_argument('-f', '--file', help='The output will be saved whith this name. If this option is not selected the output is saved in the file "scientific_name".fa (e.g. zma.fa, hsa.fa).')

args=parser.parse_args()

organisms_file=args.organisms_file
all_miRNAs_file=args.miRBase_fasta_file
filter_string=args.scientific_name

if args.file:
	output_file=args.file
else:
	output_file=filter_string.replace(' ','_')+'.fa'

# Select the correct column in the file
if args.o:
	index=0
elif args.t:
	index=3
else:
	index=2


species=parse_species_list(organisms_file,filter_string,index)
filter_file(all_miRNAs_file,species,filter_string)

