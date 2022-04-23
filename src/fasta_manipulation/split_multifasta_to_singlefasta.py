# python3
import os
import sys
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-mfa", "--multifasta", required=True,  help="input multi-fasta file to split to single-fasta")
ap.add_argument("-dir", "--directory", required=False, default='.', type=str, help="output directory to save the single-fasta files. Default is the current directory")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import multi-fasta file
features = Fasta(args['multifasta'])
# select output directory
os.chdir(args['directory'])
# export each record to a single-fasta    
for key in features.keys():
    sys.stdout = open(''.join([str(key),".fasta"]), 'a')
    print(''.join([">",str(key)]))
    print('\n'.join(split_every_60(features[str(key)][:].seq)))
    sys.stdout.close()
