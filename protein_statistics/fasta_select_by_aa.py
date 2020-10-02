# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-max", "--max_aa", required=True, help="max threshold of aa content, type = float")
ap.add_argument("-min", "--min_aa", required=True, help="min threshold of aa content, type = float")
ap.add_argument("-aa", "--aa_type", required=True, help="aa to search the content for")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
# create aa_content function
def aa_content(seq):
  return round((seq.count(args['aa_type']) / len(seq)) * 100, 2)
# main
sequences = []  # setup an empty list
for record in SeqIO.parse(args['input_file'], "fasta"):
    if float(args['min_aa']) < aa_content(record.seq) < float(args['max_aa']):
        # add this record to the list
        sequences.append(record)

print("retrieved %i sequences" % len(sequences))

SeqIO.write(sequences, args['output_file'], "fasta")

