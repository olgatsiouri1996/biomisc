# python3
import argparse
import os
import sys
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-id", "--identifier", required=True, type=str, help="fasta identifier to retrieve the fasta sequence for")
ap.add_argument("-dir", "--directory", required=False, default='.', type=str, help="output directory to save the single-fasta file.")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import multi-fasta file
features = Fasta(args['input'])
# extract 1 fasta record based on a fasta identifier
os.chdir(args['directory'])
sys.stdout = open(''.join([args['identifier'],".fasta"]), 'a')
print(''.join([">",features[args['identifier']].long_name]).replace('\r', ''))
print('\n'.join(split_every_60(features[args['identifier']][:].seq)))
sys.stdout.close()

