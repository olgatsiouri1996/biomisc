# python3
import os
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file(default 1)")
ap.add_argument("-stop", "--stop", required=True, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
args = vars(ap.parse_args())
# main
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
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        # read each file, trim and create SeqRecord to export
        record = SeqIO.read(filename, "fasta")
        sequence = record[seq_start:seq_end]
        # export to fasta
        SeqIO.write(sequence, "".join([filename.split(".")[0],"_","trimmed",".fasta"]), "fasta")

