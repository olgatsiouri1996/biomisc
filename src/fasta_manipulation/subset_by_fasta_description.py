# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-ma", "--match", required=True, type=str, help="word or phrase to search in each fasta header")
ap.add_argument("-out", "--output", required=True, help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# iterate input headers to extract sequences and export as multi-fasta
sys.stdout = open(args['output'], 'a')
for header in features.keys():
    if args['match'] in features[str(header)].long_name:
        print(''.join([">",features[str(header)].long_name]))
        print('\n'.join(split_every_60(features[str(header)][:].seq)))
sys.stdout.close()

