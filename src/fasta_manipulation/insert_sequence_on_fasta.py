# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser(description="insert a sequence at a specific position in a single-fasta file")
ap.add_argument("-in", "--input", required=True, help="input single-fasta file")
ap.add_argument("-is", "--insert", required=True, help="input single-fasta file with the sequence to insert")
ap.add_argument("-pos", "--position", required=True, type=int, help="position in the fasta file after which to insert the sequence")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# retrieve insert sequence
ist = Fasta(args['insert'],as_raw=True)
sequence = [ist[key][:] for key in ist.keys()]
# split inport fasta to 2 part to concat the inserted part later
# part a
suba = [features[key][:args['position']].seq for key in features.keys()]
# part b
subb = [features[key][args['position']:].seq for key in features.keys()]
merged_seq = ''.join([suba[0],sequence[0],subb[0]])
# export
sys.stdout = open(args['output'], 'w')
for key in features.keys():
    print(''.join([">",features[key].long_name]).replace('\r', ''))
    print('\n'.join(split_every_60(merged_seq)))
sys.stdout.close()
