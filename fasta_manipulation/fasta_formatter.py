# python3
import argparse
from Bio import SeqIO
import sys
# input parameters
ap = argparse.ArgumentParser(description="changes the width of sequences line in a FASTA file")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
ap.add_argument("-width", "--width", required=False, type=int, default=80, help="number of characters per line. Default 80")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters
def split_every_width(s): return [s[i:i+args['width']] for i in range(0,len(s),args['width'])]
# export to a new fasta file
sys.stdout = open(args['output'], 'a')
for record in SeqIO.parse(args['input'],'fasta'):
	print(">"+record.id)
	print('\n'.join(split_every_width(str(record.seq)))) # add characters in new line after the number of characters surpasses the input width 
sys.stdout.close()
