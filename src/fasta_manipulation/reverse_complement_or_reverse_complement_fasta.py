# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program", required=False, default=1, type=int, help="program to choose 1. reverse complement, 2. reverse, 3. complement. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
# select program
if args['program'] == 1:
    for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the list
        record.seq = record.seq.reverse_complement()
        sequences.append(record)
        SeqIO.write(sequences, args['output'], "fasta")
elif args['program'] == 2:
    for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the list
        sequences.append(record[::-1])
        SeqIO.write(sequences, args['output'], "fasta")
else:
    for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the list
        record.seq = record.seq.complement()
        sequences.append(record)
        SeqIO.write(sequences, args['output'], "fasta")

