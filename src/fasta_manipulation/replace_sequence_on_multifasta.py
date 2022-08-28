# python3
import argparse
import sys
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser(description="replace subsequences with new one's in a multi-fasta file")
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-is", "--insert", required=True,  help="input single-fasta file with the sequence to insert")
ap.add_argument("-pos", "--position", required=True,  help="tab seperated 3-column txt file with id and positions (start position after which to insert the sequence end position after witch the original sequence stays the same) as columns")
ap.add_argument("-out", "--output", required=True, help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# setup empty lists
ids = []
start = []
end = []
# import txt with positions
with open(args['position'], 'r') as f:
    for line in f:
        # convert each column to list
        ids.append(line.split()[0])
        start.append(line.split()[1])
        end.append(line.split()[2])
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# retrieve insert sequence
ist = Fasta(args['insert'],as_raw=True)
sequence = [ist[key][:] for key in ist.keys()]
# split inport fasta to 2 part to concat the inserted part later
# part a
suba = [features[str(a)][:int(b)].seq for (a, b) in zip(ids, start)]
# part b
subb = [features[str(a)][int(b):].seq for (a, b) in zip(ids, end)]
merged_seqs = [''.join([str(a),sequence[0],str(b)]) for (a, b) in zip(suba, subb)]
# export
sys.stdout = open(args['output'], 'w')
for (a, b) in zip(ids, merged_seqs):
    print(''.join([">",features[str(a)].long_name]).replace('\r', ''))
    print('\n'.join(split_every_60(str(b))))
sys.stdout.close()
