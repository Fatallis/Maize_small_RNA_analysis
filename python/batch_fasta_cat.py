#!/usr/bin/python
import HTSeq, sys, os, argparse, glob, subprocess, multiprocessing
from joblib import Parallel, delayed

# Traverses the list of directories
def list_subdirectories(pathname):
	for dirname, dirnames, filenames in os.walk('.'):
		# print path to all subdirectories first.
		for subdirname in dirnames:
			yield (os.path.join(dirname, subdirname))

# Executes fasta_cat.py on every subdirectory
def fasta_cat(subdirectory):
	prename=subdirectory[5:]
	filename='ok_'+prename+'.fasta'
	FNULL=open(os.devnull,'w')
	command=['fasta_cat.py','-c','-d',filename,'-t',subdirectory]
	p=subprocess.call(command,stdout=FNULL,stderr=subprocess.STDOUT)

# List of zm subdirectories (zm Harcoded)
subs=[d for d in list_subdirectories('.') if d.startswith('./zm')]

# Executes the commands in parallel
num_cores=multiprocessing.cpu_count()
Parallel(n_jobs=num_cores)(delayed(fasta_cat)(s) for s in subs)

