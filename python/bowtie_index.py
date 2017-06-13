#!/usr/bin/python
import HTSeq, sys, os, argparse, glob, subprocess, multiprocessing
from joblib import Parallel, delayed

# Traverse the subdirectorie tree
def list_ok_fasta_files(pathname,extension):
	for root, dirnames, filenames in os.walk(pathname):
		for filename in filenames:
			if filename.endswith(extension) and 'ok' in filename:
				relDir=os.path.relpath(root, pathname)
				relFile=os.path.join(relDir, filename)

				yield relFile

# Run the system command to build bowtie index
def build_bowtie_index(fasta):
	print 'Processing '+fasta
	outpath=get_filename(fasta)
	FNULL=open(os.devnull,'w')
	command=['bowtie-build','-f', fasta, outpath]
	p=subprocess.call(command,stdout=FNULL,stderr=subprocess.STDOUT)

# Remove the '.fasta' extension from the fastafile name
def get_filename(filepath):
	return filepath[:-6]

# Define command-line options
parser=argparse.ArgumentParser(description="This script creates a bowtie index file for every fasta file with '.fasta' extension in the subdirectories on DIR")
parser.add_argument('DIR',help='DIR is the directory where bowtie indexes for every .fasta file found including subdirectories.')
args=parser.parse_args()

dirpath=args.DIR

# Creates the bowtie indexes in parallel
num_cores=multiprocessing.cpu_count()
files_list=[fasta for fasta in list_ok_fasta_files(dirpath,'fasta')]
Parallel(n_jobs=num_cores)(delayed(build_bowtie_index)(fasta) for fasta in files_list)
