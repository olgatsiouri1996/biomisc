# python3
import argparse
from Bio import SeqIO
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
ap.add_argument("-max", "--max_number", required=True, help="max number of nucleotide/protein length")
ap.add_argument("-min", "--min_number", required=True, help="min number of nucleotide/protein length")
ap.add_argument("-headers", "--fasta_headers", required=True, help="file to save the output fasta headers")
args = vars(ap.parse_args())

# main
sequences = []  # setup an empty list
for record in SeqIO.parse(args['input_file'], "fasta"):
    if int(args['min_number']) < len(record.seq) < int(args['max_number']):
        # add this record to the list
        sequences.append(record)

print("retrieved %i sequences" % len(sequences))

SeqIO.write(sequences, args['output_file'], "fasta")
# retrieve headers only
headers = []  # setup an empty list
for record in SeqIO.parse(args['input_file'], "fasta"):
    if int(args['min_number']) < len(record.seq) < int(args['max_number']):
        # add this record to the list
        headers.append(record.id)
with open(args['fasta_headers'], 'w') as filehandle:
    for listitem in headers:
        filehandle.write('%s\n' % listitem)

