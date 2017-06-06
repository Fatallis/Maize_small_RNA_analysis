#!/usr/bin/python
import HTSeq, sys, os, argparse, glob

# Converts a sequence from RNA to DNA
def rna2dna(seq):
	seq.seq=seq.seq.replace('U','T')
	seq.seq=seq.seq.replace('u','t')
	return seq

# Define command-line interface
parser=argparse.ArgumentParser(description="This script concatenates al fasta files with '.fa' extension in the current directory into the OUTPUT file.")
parser.add_argument('OUTPUT',help='OUTPUT fasta file.')
parser.add_argument('-t', '--TARGET', help='The fasta files will be searched instead in the TARGET directory, the OUTPUT file will be saved also in the TARGET directory.')
parser.add_argument('-d', '--DNA', action='store_true', help='Changes RNA to DNA')
parser.add_argument('-c', '--COLLAPSE', action='store_true', help='Reduce from multiple repeated sequences to multiple unique sequences.')

args=parser.parse_args()

path='.'
outfile=args.OUTPUT

if args.TARGET:
	if args.TARGET.endswith(os.sep):
		path=args.TARGET+path
		outfile=args.TARGET+outfile
	else:
		path=args.TARGET+os.sep+path
		outfile=args.TARGET+os.sep+outfile

seqs=dict()

with open(outfile,'w') as outfile:
	for f in os.listdir(path):
		if f.endswith(".fa"):
			if args.TARGET:
				if args.TARGET.endswith(os.sep):
					f=args.TARGET+f
				else:
					f=args.TARGET+os.sep+f
			for seq in HTSeq.FastaReader(f):
				seq.seq=seq.seq.upper()
				if args.DNA:
					seq=rna2dna(seq)

				if args.COLLAPSE:
					if seq.seq not in seqs:
						seqs[seq.seq]=1
					else:
						seqs[seq.seq]+=1
				else:
					seq.write_to_fasta_file(outfile)

	if args.COLLAPSE:
		for i, s in enumerate(sorted(seqs, key=seqs.get, reverse=True)):
			name=str(i+1)+'-'+str(seqs[s])
			seq=s
			new_seq=HTSeq.Sequence(seq,name)
			new_seq.write_to_fasta_file(outfile)

