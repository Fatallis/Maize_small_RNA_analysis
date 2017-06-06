#!/usr/bin/python
import HTSeq, sys, os, argparse, glob, subprocess, multiprocessing

# Traverse the directory list
def list_ok_fasta_files(pathname,extension):
	for root, dirnames, filenames in os.walk(pathname):
		for filename in filenames:
			if filename.endswith(extension):
				relDir=os.path.relpath(root, pathname)
				relFile=os.path.join(relDir, filename)

				yield relFile

# Classifies the different fasta files in the corresponding RNA types
def process_rnas(f):
	prename=f[2:-4]
	destiny='../zm_'+prename
	with open(f) as infile:
		for line in infile:
			line=line.strip()
			fasta_name='zm_'+line+'.fa'
			if os.path.exists(fasta_name):
				os.rename(fasta_name, destiny+'/'+fasta_name)


files_list=[f for f in list_ok_fasta_files('.','rna')]

for f in files_list:
	process_rnas(f)

