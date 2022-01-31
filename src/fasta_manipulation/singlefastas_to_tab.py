# python3
import os
import argparse
from Bio import SeqIO
import pandas as pd
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-out","--output", required=True, help="output txt file")
args = vars(ap.parse_args())
# main
seqs = []
ids = [] # setup empty lists
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
	if filename.endswith(".fa") or filename.endswith(".fasta"):
		for record in SeqIO.parse(filename, "fasta"):
			ids.append(record.id)
			seqs.append(record.seq)
# put the 2 list in a data frame of 2 columns
dfasta = pd.DataFrame()
dfasta['id'] = ids
dfasta['seq'] = seqs
# export data frame to a tabular txt file
with open(args['output'], 'a') as f:
    f.write(
        dfasta.to_csv(header = False, index = False, sep= "\t", line_terminator= '\n')
    )
