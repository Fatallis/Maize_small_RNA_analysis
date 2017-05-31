#!/usr/bin/python
import HTSeq, sys, os, argparse, multiprocessing
from joblib import Parallel, delayed

# Argparse section
parser=argparse.ArgumentParser(prog='sort_fasta', description='This script filters the fasta records in files corresponding to each group of genomic features found.')
parser.add_argument('fasta_file',help='Fasta file obtained from Bedtools getfasta option.')
args=parser.parse_args()

# Fasta file input
fasta=args.fasta_file

# Get the filename
filename=os.path.splitext(fasta)[0]

# Get the set of names in the fasta records
names=set()
for record in HTSeq.FastaReader(fasta):
	if record.name not in names:
		names.add(record.name)


# Create a dictionary with the name of the different genomic features
records=dict()
for name in names:
	records[name]=list()

# Sort the fasta records into the corresponding group
for record in HTSeq.FastaReader(fasta):
	records[record.name].append(record)

# Save the records in different fasta files
for r in records:
	with open(filename+'_'+r+'.fa','w') as fastafile:
		for record in records[r]:
			record.write_to_fasta_file(fastafile)

