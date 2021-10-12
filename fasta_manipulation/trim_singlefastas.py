# python3
import os
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-start", "--start_fasta", required=True, type=int, help="region to start writing the fasta file(min number 0)")
ap.add_argument("-stop", "--stop_fasta", required=True, type=int, help="region to stop writing the fasta file(negative number to remove nucleotides from the end of the sequence")
args = vars(ap.parse_args())
# main
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        # read each file, trim and create SeqRecord to export
        record = SeqIO.read(filename, "fasta")
        sequence = record[args['start_fasta']:args['stop_fasta']]
        # export to fasta
        SeqIO.write(sequence, "".join([filename.split(".")[0],"_","trimmed",".fasta"]), "fasta")

