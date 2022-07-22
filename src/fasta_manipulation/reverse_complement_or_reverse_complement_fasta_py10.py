# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program", required=False, default=1, type=int, help="program to choose 1. reverse complement, 2. reverse, 3. complement. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# select program
program = args['program']
match program:
    case 1:
        sys.stdout = open(args['output'], 'a')
        for key in features.keys():
            print(''.join([">",features[key].long_name]))
            print('\n'.join(split_every_60(features[str(key)][:].reverse.complement.seq)))
        sys.stdout.close()
    case 2:
        sys.stdout = open(args['output'], 'a')
        for key in features.keys():
            print(''.join([">",features[key].long_name]))
            print('\n'.join(split_every_60(features[key][:].reverse.seq)))
        sys.stdout.close()
    case 3:
        sys.stdout = open(args['output'], 'a')
        for key in features.keys():
            print(''.join([">",features[key].long_name]))
            print('\n'.join(split_every_60(features[key][:].complement.seq)))
        sys.stdout.close()
