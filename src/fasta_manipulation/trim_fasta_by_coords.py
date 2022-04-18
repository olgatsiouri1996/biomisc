# python3
import sys
import argparse
from pyfaidx import Fasta
import  pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=False, help="input fasta file")
ap.add_argument("-coords", "--coordinates", required=True, help="input 4-column tab-seperated txt file with id, start, end positions and strand(+, -) respectively in each row")
ap.add_argument("-out", "--output", required=False, help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# inport txt file and convert each column to list
df_txt = pd.read_csv(args['coordinates'], header=None, sep="\t")
ids = df_txt.iloc[:,0].values.tolist()
seq_start = df_txt.iloc[:,1].values.tolist()
seq_start[:] = [i - 1 for i in seq_start]
seq_end = df_txt.iloc[:,2].values.tolist()
seq_strand = df_txt.iloc[:,3].values.tolist()
# setup empty list
trimmed_records = []
# import fasta file
features = Fasta(args['input'])
# iterate all below lists in pairs
sys.stdout = open(args['output'], 'a')
for (a, b, c, d) in zip(ids, seq_start, seq_end, seq_strand):
    if str(d) == "+":
        print(''.join([">",str(a),"_",str(int(b) + 1),"_",str(c)]))
        print('\n'.join(split_every_60(features[str(a)][int(b):int(c)].seq)))
    else:
        print(''.join([">",str(a),"_",str(int(b) + 1),"_",str(c),"_","complement"]))
        print('\n'.join(split_every_60(features[str(a)][int(b):int(c)].complement.seq)))
sys.stdout.close()
