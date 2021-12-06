# python3
import os
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in","--input", required=True, help="input multi-fasta file")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file(default 1)")
ap.add_argument("-stop", "--stop", required=False, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose 1) add both start and stop location 2) the stop location with be that of the sequence length. Default is 1")
ap.add_argument("-out","--output", required=True, help="output txt file")
args = vars(ap.parse_args())
# main
# create function to trim fasta records
def fastatrim(fastaseq):
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
        args['stop'] = len(fastaseq)
        seq_end = args['stop']
    # subset each fasta record
    return fastaseq[seq_start:seq_end]
# setup empty lists
seqs = []
ids = []
# import each fasta file from the working directory
for record in SeqIO.parse(args['input'], "fasta"):
    seqs.append(fastatrim(record.seq))
    ids.append(record.id)
# put the 2 list in a data frame of 2 columns
dfasta = pd.DataFrame()
dfasta['id'] = ids
dfasta['seq'] = seqs
# export data frame to a tabular txt file
with open(args['output'], 'a') as f:
    f.write(
        dfasta.to_csv(header = False, index = False, sep= "\t", line_terminator= '\n')
    )       
