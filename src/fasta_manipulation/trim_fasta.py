# python3
import os
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser() 
ap.add_argument("-in", "--input", required=False , help="input fasta file")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file. Default is 1")
ap.add_argument("-stop", "--stop", required=False, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
ap.add_argument("-dir", "--directory", required=False, type=str, help="directory to search for fasta files")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose: 1) add both start and stop location 2) the stop location will be that of the sequence length. Default is 1")
ap.add_argument("-type", "--type", required=False,default=1, type=int,  help="type of fasta to import: 1) 1 multi-fasta file 2) many single-fasta files. Default is 1")
ap.add_argument("-out", "--output", required=False, help="output fasta file")
args = vars(ap.parse_args())
# main
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
        seq_end = len(fastaseq)
    # subset each fasta record
    return fastarec[seq_start:seq_end]
# choose fasta type to import
if args['type'] == 1:    
    # setup an empty list
    sequences = []  
    # iterate for each record
    for record in SeqIO.parse(args['input'], "fasta"):
            # add this record to the list
        sequences.append(fastatrim(record,record.seq))
    # export to fasta
    SeqIO.write(sequences, args['output'], "fasta")
else:
    # import each fasta file from the working directory
    for filename in sorted(os.listdir(os.chdir(args['directory']))):
        if filename.endswith(".fa") or filename.endswith(".fasta"):
            # read each file, trim and create SeqRecord to export
            record = SeqIO.read(filename, "fasta")
            sequence = fastatrim(record,record.seq)
            if args['program'] ==1:
                if args['stop'] > 0:
                    # export to fasta
                    SeqIO.write(sequence, "".join([filename.split(".")[0],"_",str(args['start']),"_",str(args['stop']),".fasta"]), "fasta")
                else:
                    SeqIO.write(sequence, "".join([filename.split(".")[0],"_",str(args['start']),"_",str(len(sequence.seq)),".fasta"]), "fasta")
            else:
                SeqIO.write(sequence, "".join([filename.split(".")[0],"_",str(args['start']),"_",str(len(record.seq)),".fasta"]), "fasta")

