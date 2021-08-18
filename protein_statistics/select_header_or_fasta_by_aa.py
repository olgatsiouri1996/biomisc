# python3
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-pro", "--program",type=int, default=1, required=False, help="choose to output a fasta file or a txt file with headers(1.fasta, 2.txt file with headers. Defaults to 1)")
ap.add_argument("-max", "--max_aa", required=True, help="max threshold of aa content, type = float")
ap.add_argument("-min", "--min_aa", required=True, help="min threshold of aa content, type = float")
ap.add_argument("-aa", "--aa_type", required=True, help="aa to search the content for")
ap.add_argument("-headers", "--fasta_headers", required=False, help="file to save the output fasta headers")
ap.add_argument("-out", "--output_file", required=False, help="output fasta file")
args = vars(ap.parse_args())
# create aa_content function
def aa_content(seq):
    return round((seq.count(args['aa_type']) / len(seq)) * 100, 2)
# main
# choose program
program = args['program']
# select sequences
if program == 1:
    sequences = []  # setup an empty list
    for record in SeqIO.parse(args['input_file'], "fasta"):
        if float(args['min_aa']) < aa_content(record.seq) < float(args['max_aa']):
            # add this record to the list
            sequences.append(record)
    # export to fasta
    SeqIO.write(sequences, args['output_file'], "fasta")
# retrieve headers only
elif program == 2:
    headers = []  # setup an empty list
    for record in SeqIO.parse(args['input_file'], "fasta"):
        if float(args['min_aa']) < aa_content(record.seq) < float(args['max_aa']):
            # add this record to the list
            headers.append(record.id)
    # export to txt
    with open(args['fasta_headers'], 'w') as filehandle:
        for listitem in headers:
            filehandle.write('%s\n' % listitem)


