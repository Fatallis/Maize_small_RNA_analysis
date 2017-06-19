#!/usr/bin/python
import HTSeq, sys, os, argparse, glob, subprocess, multiprocessing
from joblib import Parallel, delayed

# Tarverse the full directory and subdirectories list
def list_files(pathname, pattern):
	for file in os.listdir(pathname):
		if pattern in file:
			yield file

# Execute count_reads.py for each file
def count_reads(fasta):
	command=['count_reads.py',fasta]
	p=subprocess.Popen(command,stdout=subprocess.PIPE)
	outs,errs=p.communicate()
	return outs

# cmmand-line help for ue this script
parser=argparse.ArgumentParser(description="This script take all the fasta files that have the 'PATTERN' in its name to count the sequences contained in the files.")
parser.add_argument('PATTERN', help='The common PATTERN in the input filenames.')
parser.add_argument('-t','--test',action='store_true',help='Print the files to be counted')

args=parser.parse_args()

# Colect list of files with PATTERN
files=[f for f in sorted(list_files('.',args.PATTERN))]

# Run the main script
if args.test:
	for f in files:
		print 'INPUT is: '+f

else:
	num_cores=multiprocessing.cpu_count()
	results=Parallel(n_jobs=num_cores)(delayed(count_reads)(f) for f in sorted(files))

	for r in sorted(results):
		print r

