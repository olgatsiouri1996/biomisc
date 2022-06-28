# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser(description="reverse complement or reverse some sequences in a multi-fasta file")
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-ids", "--ids", required=True, help="file with fasta headers to reorient some output fasta sequences")
ap.add_argument("-pro", "--program", required=False, default=1, type=int, help="program to choose 1. reverse complement, 2. reverse. Default is 1")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
# import the txt file with headers you want to reorient the sequence from the input multi-fasta
with open(args['ids'], 'r') as f:
    headers = f.readlines()
headers = [x.strip() for x in headers]
# setup an empty list
sequences = [] 
# choose program
if args['program'] == 1:
    for record in SeqIO.parse(args['input_file'], "fasta"):
        if record.id in headers:
            # add this record to the list
            record.seq = record.seq.reverse_complement()
            sequences.append(record)
        else:
            sequences.append(record)
# export to fasta
    SeqIO.write(sequences, args['output_file'], "fasta")
else:
    for record in SeqIO.parse(args['input_file'], "fasta"):
        if record.id in headers:
            # add this record to the list
            sequences.append(record[::-1])
        else:
            sequences.append(record)
# export to fasta
    SeqIO.write(sequences, args['output_file'], "fasta")

