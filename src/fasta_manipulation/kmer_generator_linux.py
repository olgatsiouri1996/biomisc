# python3
import argparse
from Bio import SeqIO
import pandas as pd
import os
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-step", "--step_size", required=True, help="step size to split fasta, type = int")
ap.add_argument("-win", "--window_size", required=True, help="window size of splitted subsets, type = int")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
sequences = []
headers = [] # setup empty lists
for record in SeqIO.parse(args['input_file'], "fasta"):
    for i in range(0, len(record.seq) - int(args['window_size']) + 1, int(args['step_size'])):
        sequences.append(record.seq[i:i + int(args['window_size'])])
        headers.append(i)
# create data frame
df = pd.DataFrame()
df['id'] = headers
df['seq'] = sequences
# export
with open("out.tab", 'a') as f:
    f.write(
        df.to_csv(header = False, index = False, sep = '\t', doublequote= False, line_terminator= '\n')
    )

# convert to fasta
count = SeqIO.convert("out.tab", "tab", args['output_file'], "fasta")
os.system("rm out.tab")
