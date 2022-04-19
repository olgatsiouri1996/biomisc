# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-ids", "--ids", required=True, help="file with fasta headers to retrieve the output fasta sequences")
ap.add_argument("-out", "--output", required=True, help="output multi-fasta file")
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
# iterate input headers to extract sequences and export as multi-fasta
sys.stdout = open(args['output'], 'a')
for header in headers:
    print(''.join([">",str(header)]))
    print('\n'.join(split_every_60(features[str(header)][:].seq)))
sys.stdout.close()
