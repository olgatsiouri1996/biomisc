# python3
import sys
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser(description = "add a left or right adapter or both by indexing a single or multi-fasta file")
ap.add_argument("-in", "--input", required=True,  help="input single or multi fasta file")
ap.add_argument("-le", "--left", required=False, type=str, default="",  help="adapter to the left of the sequence. Default is no left adapter sequence to add")
ap.add_argument("-ri", "--right", required=False, type=str, default="",  help="adapter to the right of the sequence. Default is no right adapter sequence to add")
ap.add_argument("-out", "--output", required=True, help="output single or multi-fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# merge sequences and export to fasta
sys.stdout = open(args['output'], 'a')
for key in features.keys():
    print(''.join([">",features[key].long_name]))
    print('\n'.join(split_every_60(args['left'] + features[key][:].seq + args['right'])))
sys.stdout.close()