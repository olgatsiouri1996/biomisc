# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file(default 1)")
ap.add_argument("-stop", "--stop", required=True, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
# fix the index for start parameter
if args['start'] > 0:
    seq_start = args['start'] -1
else:
    print("-start parameter must be a positive integer")
    exit(1)
# fix the index for end parameter
if args['stop'] > 0:
    seq_end = args['stop'] -1
else:
    seq_end = args['stop']
# iterate for each record
for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the list
    sequences.append(record[seq_start:seq_end])

# export to fasta
SeqIO.write(sequences, args['output'], "fasta")

