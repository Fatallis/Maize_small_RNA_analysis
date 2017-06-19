#!/usr/bin/python
import HTSeq, sys, os, argparse, glob, subprocess, multiprocessing, re

# Command-line to help the usage of this script
parser=argparse.ArgumentParser(description="This script counts all the sequences in the INPUT file.")
parser.add_argument('INPUT',help='INPUT fasta file.')
args=parser.parse_args()

infile=args.INPUT

# Count total reads
def total_reads(infile):
	p1=subprocess.Popen(['more', infile], stdout=subprocess.PIPE)
	p2=subprocess.Popen(['grep', '^>'], stdin=p1.stdout, stdout=subprocess.PIPE)
	p3=subprocess.Popen(['cut','-d','-','-f2'], stdin=p2.stdout, stdout=subprocess.PIPE)
	p4=subprocess.Popen(['paste','-sd+','-'], stdin=p3.stdout, stdout=subprocess.PIPE)
	p5=subprocess.Popen(['bc'], stdin=p4.stdout, stdout=subprocess.PIPE)
	output,err = p5.communicate()
	return output.strip()

# Count unique reads
def unique_reads(infile):
	p1=subprocess.Popen(['more', infile], stdout=subprocess.PIPE)
	p2=subprocess.Popen(['grep','-c','^>'], stdin=p1.stdout, stdout=subprocess.PIPE)
	output,err=p2.communicate()
	return output.strip()

# Return the cunts of unique and total reads
print infile
print 'Unique reads:\t'+unique_reads(infile)
print 'Total reads:\t'+total_reads(infile)
