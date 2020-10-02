# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
ap.add_argument("-headers", "--fasta_headers", required=True, help="file with fasta headers to retrieve the output fasta sequences")
args = vars(ap.parse_args())
# main
wanted = set()
with open(args['fasta_headers']) as f:
    for line in f:
        line = line.strip()
        if line != "":
            wanted.add(line)

fasta_sequences = SeqIO.parse(open(args['input_file']),'fasta')
with open(args['output_file'], "w") as f:
    for seq in fasta_sequences:
        if seq.id not in wanted:
            SeqIO.write([seq], f, "fasta")
