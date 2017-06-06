#!/usr/bin/python
import argparse, HTSeq

# Define command-line interface
parser=argparse.ArgumentParser(description="This script filter all fasta records with STRING in their names into the OUTPUT file.")
parser.add_argument('INPUT',help='INPUT fasta file.')
parser.add_argument('OUTPUT',help='OUTPUT fasta file.')
parser.add_argument('STRING',help='STRING to search in the names of the fasta records.')
parser.add_argument('-l','--list',action='store_true',help='if the LIST option is enabled, STRING must be a file with a list of names to be filtered.')
parser.add_argument('-r','--reverse',action='store_true',help='if this option is enabled, the selection of the records is inverted.')

args=parser.parse_args()

fasta=args.INPUT
outfile=args.OUTPUT
s=args.STRING


with open(outfile, 'w') as outfile:
	if args.list:
		with open(s) as ln:
			names=[n.strip() for n in ln]
			for seq in HTSeq.FastaReader(fasta):
				if not args.reverse:

					##### Added on Apr 18 2017 Revise if works well with the previous work
					if any(name in seq.name for name in names):
						seq.write_to_fasta_file(outfile)
					##### Added on Apr 18 2017


					if seq.name in names:
						seq.write_to_fasta_file(outfile)
				else:
					if seq.name not in names:
						seq.write_to_fasta_file(outfile)
	else:
		for seq in HTSeq.FastaReader(fasta):
			if not args.reverse:
				if s in seq.name or s in seq.descr:
					seq.write_to_fasta_file(outfile)
			else:
				if not s in seq.name and not s in seq.descr:
					seq.write_to_fasta_file(outfile)
