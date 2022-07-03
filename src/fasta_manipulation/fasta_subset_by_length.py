# python3
import argparse
from Bio import SeqIO
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program",type=int, default=1, required=False, help="choose to output a fasta file or a txt file with headers(1.fasta file with sequence length in fasta description, 2.txt file with headers. Defaults to 1)")
ap.add_argument("-out", "--output", required=False, help="output fasta file")
ap.add_argument("-max", "--max", required=False, default=300, help="max number of sequence length. Default is 300")
ap.add_argument("-min", "--min", required=False, default=1, help="min number of sequence length. Default is 1")
ap.add_argument("-headers", "--headers", required=False, help="file to save the output fasta headers")
args = vars(ap.parse_args())

# main
# choose program
program = args['program']
# select sequences
if program == 1:
    sequences = []  # setup an empty list
    for record in SeqIO.parse(args['input'], "fasta"):
        if int(args['min']) <= len(record.seq) <= int(args['max']):
            # add this record to the list
            print(record.description)
            record.description = ''.join(["sequence length:"," ",str(len(record.seq))," ",str(record.description).split(record.id)[1]])
            sequences.append(record)
    # export to fasta
    SeqIO.write(sequences, args['output'], "fasta")
# retrieve headers only
else:
    headers = []  # setup an empty list
    for record in SeqIO.parse(args['input'], "fasta"):
        if int(args['min']) <= len(record.seq) <= int(args['max']):
            # add this record to the list
            headers.append(record.id)
    # export to txt
    with open(args['headers'], 'w') as filehandle:
        for listitem in headers:
            filehandle.write('%s\n' % listitem)

