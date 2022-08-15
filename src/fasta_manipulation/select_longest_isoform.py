# python 3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create fasta index
features = Fasta(args['input'],split_char=".", duplicate_action="longest")
# select sequences
sys.stdout = open(args['output'], 'a')
for key in features.keys():
    print(''.join([">",features[key].long_name]).replace('\r', ''))
    print('\n'.join(split_every_60(features[key][:].seq)))
sys.stdout.close()
