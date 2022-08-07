# python3
import sys
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa1", "--fasta1", required=True, help="input multi fasta file with fasta descriptions to filter by")
ap.add_argument("-fa2", "--fasta2", required=True, help="input multi fasta file to retrieve the sequences whose fasta identifier intersects with fasta1")
ap.add_argument("-ma", "--match", required=True, type=str, help="word or phrase to search in each fasta header(no regular expression, differentiates between capital or non capital letters)")
ap.add_argument("-out", "--output", required=True, help="output multi fasta file. File can be appended")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create fasta index
features1 = Fasta(args['fasta1'])
features2 = Fasta(args['fasta2'])
# export to fasta
sys.stdout = open(args['output'], 'a')
# iterate the following 2 lists
for key in features1.keys():
    if args['match'] in features1[key].long_name:
        print(''.join([">",features2[key].long_name]))
        print('\n'.join(split_every_60(features2[key][:].seq)))
sys.stdout.close()

