# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser(description="reverse the sequences of a multi or single-fasta file")
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
for record in SeqIO.parse(args['input_file'], "fasta"):
    # add this record to the list
    sequences.append(record[::-1])
SeqIO.write(sequences, args['output_file'], "fasta")
