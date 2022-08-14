# python3
import argparse
from pyfaidx import Fasta
import sys
# input parameters
ap = argparse.ArgumentParser(description="indexes the input fasta file for memory efficiency and changes the width of fasta sequences")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
ap.add_argument("-width", "--width", required=False, type=int, default=80, help="number of characters per line. Default is  80")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters
def split_every_width(s): return [s[i:i+ args['width']] for i in range(0,len(s),args['width'])]
# import fasta file
features = Fasta(args['input'])
# extract a fasta file with a new line width
sys.stdout = open(args['output'], 'a')
for key in features.keys():
    print(''.join([">",features[key].long_name]).replace('\r',''))
    print('\n'.join(split_every_width(features[key][:].seq)))
sys.stdout.close()

