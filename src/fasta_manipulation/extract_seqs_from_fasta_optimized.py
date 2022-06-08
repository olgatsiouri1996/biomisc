# python3
import os
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-ids", "--ids", required=True, help="file with fasta headers to retrieve the output fasta sequences")
ap.add_argument("-out", "--output", required=False, help="output multi-fasta file")
ap.add_argument("-dir", "--directory", required=False, type=str, default='.', help="output directory to save the single-fasta files. Default is the current directory")
ap.add_argument("-pro", "--program",type=int, default=1, required=False, help="choose to exract: 1) a multi-fasta file, 2) many single-fasta files. Defaults to 1")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import the txt file with headers you want to extract the sequence from the input fasta
with open(args['ids'], 'r') as f:
    headers = f.readlines()
headers = [x.strip() for x in headers]
# import fasta file
features = Fasta(args['input'])
# choose program
program = args['program']
# extract a multi-fasta file
if program == 1:           
    # iterate input headers to extract sequences and export as multi-fasta
    sys.stdout = open(args['output'], 'a')
    for header in headers:
        print(''.join([">",features[str(header)].long_name]))
        print('\n'.join(split_every_60(features[str(header)][:].seq)))
    sys.stdout.close()
else:
    # extract many single fasta files
    os.chdir(args['directory'])
    for header in headers:
        sys.stdout = open(''.join([str(header),".fasta"]), 'a')
        print(''.join([">",features[str(header)].long_name]))
        print('\n'.join(split_every_60(features[str(header)][:].seq)))
        sys.stdout.close()
