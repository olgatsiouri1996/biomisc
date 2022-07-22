# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-ids", "--ids", required=True, help="file with fasta headers to reorient some input fasta sequences")
ap.add_argument("-pro", "--program", required=False, default=1, type=int, help="program to choose 1. reverse complement, 2. reverse, 3. complement. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import the txt file with headers you want to reorient the sequence from the input multi-fasta
with open(args['ids'], 'r') as f:
    headers = f.readlines()
headers = [x.strip() for x in headers]
# import fasta file
features = Fasta(args['input'])
# select program
program = args['program']
match program:
    case 1:
        sys.stdout = open(args['output'], 'a')
        for key in features.keys():
            if key in headers:
                print(''.join([">",features[key].long_name]))
                print('\n'.join(split_every_60(features[str(key)][:].reverse.complement.seq)))
            else:
                print(''.join([">",features[key].long_name]))
                print('\n'.join(split_every_60(features[str(key)][:].seq)))                
        sys.stdout.close()
    case 2:
            sys.stdout = open(args['output'], 'a')
            for key in features.keys():
                if key in headers:
                    print(''.join([">",features[key].long_name]))
                    print('\n'.join(split_every_60(features[str(key)][:].reverse.seq)))
                else:
                    print(''.join([">",features[key].long_name]))
                    print('\n'.join(split_every_60(features[str(key)][:].seq)))                
            sys.stdout.close()    
    case 3:
            sys.stdout = open(args['output'], 'a')
            for key in features.keys():
                if key in headers:
                    print(''.join([">",features[key].long_name]))
                    print('\n'.join(split_every_60(features[str(key)][:].complement.seq)))
                else:
                    print(''.join([">",features[key].long_name]))
                    print('\n'.join(split_every_60(features[str(key)][:].seq)))                
            sys.stdout.close()
