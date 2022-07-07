# python3
import sys
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input single or multi fasta file")
ap.add_argument("-des", "--descriptions", required=True, help="input 1-column txt file with fasta_descriptions")
ap.add_argument("-out", "--output", required=True,  help="output fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import file with fasta descriptions
with open(args['descriptions'], 'r') as f:
    fasta_descriptions = f.readlines()
fasta_descriptions = [x.strip() for x in fasta_descriptions]
# create fasta index
features = Fasta(args['input'])
# export to fasta
sys.stdout = open(args['output'], 'a')
# iterate the following 2 lists
for (key, fasta_description) in zip(features.keys(), fasta_descriptions):
    print(''.join([">",key," ",fasta_description]))
    print('\n'.join(split_every_60(features[key][:].seq)))
sys.stdout.close()