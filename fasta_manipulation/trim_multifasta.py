# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file(default 1)")
ap.add_argument("-stop", "--stop", required=False, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose 1) add both start and stop location 2) the stop location with be that of the sequence length. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
# create function to trim fasta records
def fastatrim(fastarec,fastaseq):
    # choose program
    if args['program'] == 1:
        # fix the index for start parameter
        if args['start'] > 0:
            seq_start = args['start'] -1
        else:
            print("-start parameter must be a positive integer")
            exit(1)
        # add end parameter
        seq_end = args['stop']
    else:
        # fix the index for start parameter
        if args['start'] > 0:
            seq_start = args['start'] -1
        else:
            print("-start parameter must be a positive integer")
            exit(1)
        # add end parameter according to program 2
        args['stop'] = len(fastaseq)
        seq_end = args['stop']
    # subset each fasta record
    return fastarec[seq_start:seq_end]
# iterate for each record
for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the list
    sequences.append(fastatrim(record,record.seq))

# export to fasta
SeqIO.write(sequences, args['output'], "fasta")

