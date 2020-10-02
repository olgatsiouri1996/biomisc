# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-start", "--start_fasta", required=True, help="region to start writing the fasta file(min number 0)")
ap.add_argument("-stop", "--stop_fasta", required=True, help="region to stop writing the fasta file(negative number to remove nucleotides from the end of the sequence")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
for record in SeqIO.parse(args['input_file'], "fasta"):
        # add this record to the list
    sequences.append(record[int(args['start_fasta']):int(args['stop_fasta'])])

print("retrieved %i sequences" % len(sequences))

SeqIO.write(sequences, args['output_file'], "fasta")

