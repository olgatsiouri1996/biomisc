# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input single or multi-fasta file")
ap.add_argument("-out", "--output", required=True, help="output multi-fasta file")
ap.add_argument("-step", "--step", required=True, type=int, help="step size for chunk creation, type = integer")
ap.add_argument("-win", "--window", required=True, type=int, help="window size for chunk creation, type = integer")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create function to slice based on window and step
def slice_by_winstep(rec):
    for i in range(0, features[rec][:].end - args['window'] + 1, args['step']):
        print(''.join([">",rec,":",str(i+1),"-",str(i + args['window'])]).replace('\r', ''))
        print('\n'.join(split_every_60(features[rec][i:i + args['window']].seq)))
    return
# import multi or single-fasta file
features = Fasta(args['input'])
# iterate input headers to extract sequences and export as multi-fasta
sys.stdout = open(args['output'], 'a')
for key in features.keys():
    slice_by_winstep(key)
sys.stdout.close()
