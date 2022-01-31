# python3
import itertools
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
# input arguments
ap = argparse.ArgumentParser(description="convert each row of a tabular file with the fasta headers and sequences in each row in a multi-fasta or many single-fasta files with trimmed sequences")
ap.add_argument("-in", "--input", required=True, help="input txt file")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="region to start writing the fasta file(default 1)")
ap.add_argument("-stop", "--stop", required=False, type=int, help="region to stop writing the fasta file(it can be both a positive and  a negative number)")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose 1) add both start and stop location 2) the stop location with be that of the sequence length. Default is 1")
ap.add_argument("-type", "--type", required=False,default=1, type=int, help="type of fasta to export 1) 1 multi-fasta file 2)  many single-fasta files. Default is 1")
ap.add_argument("-out", "--output", required=False,default=1, type=int, help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# create function to trim fasta records
def fastatrim(fastaseq):
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
    return fastaseq[seq_start:seq_end]
df = pd.read_csv(args['input'], header=None, sep="\t")
# select ids and sequence columns, convert to lists
headers = df.iloc[:,0].values.tolist()
sequences = df.iloc[:,1].values.tolist()
# choose fasta type to export
if args['type'] == 1:     
    # setup empty list
    seqs_for_fasta = []
    # iter elements on pairs to export in single fasta files
    for (ids, seq) in zip(headers, sequences):
            seqs_for_fasta.append(SeqRecord(Seq(fastatrim(str(seq))),id=str(ids),description=""))
            SeqIO.write(seqs_for_fasta, args['output'], "fasta")
else:
    # iter elements on pairs to export in single fasta files
    for (ids, seq) in zip(headers, sequences):
            seq_for_fasta=SeqRecord(Seq(fastatrim(str(seq))),id=str(ids),description="")
            SeqIO.write(seq_for_fasta, "".join([str(ids),".fasta"]), "fasta")

