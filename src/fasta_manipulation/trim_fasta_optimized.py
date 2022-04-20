# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file(default 1)")
ap.add_argument("-stop", "--stop", required=False, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose 1) add both start and stop location 2) the stop location will be that of the sequence length. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create function to trim fasta records
def fastatrim(fastarec):
    # choose program
    if args['program'] == 1:
        # fix the index for start parameter
        if args['start'] > 0:
            seq_start = args['start'] -1
        else:
            print("-start parameter must be a positive integer")
            exit(1)
        # add end parameter
        seq_end = args['stop']
    else:
        # fix the index for start parameter
        if args['start'] > 0:
            seq_start = args['start'] -1
        else:
            print("-start parameter must be a positive integer")
            exit(1)
        # add end parameter according to program 2
        args['stop'] = features[fastarec][:].end
        seq_end = args['stop']
# subset each fasta record
    print(''.join([">",features[fastarec][seq_start:seq_end].fancy_name]))
    print('\n'.join(split_every_60(features[fastarec][seq_start:seq_end].seq)))
    return
# import fasta file
features = Fasta(args['input'])
# export to fasta
sys.stdout = open(args['output'], 'a')
# iterate for each record
for key in features.keys():
    fastatrim(key)
sys.stdout.close()
