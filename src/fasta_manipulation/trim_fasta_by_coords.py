# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import  pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=False, help="input fasta file")
ap.add_argument("-coords", "--coordinates", required=True, help="input 2-column tab-seperated txt file with start and end positions respectively in each row")
ap.add_argument("-type", "--type", required=False,default=1, type=int, help="type of fasta to import 1) 1 multi-fasta file 2)  many single-fasta files. Default is 1")
ap.add_argument("-outdir", "--outdir", required=False, type=str, default='.', help="directory to save output fasta files")
ap.add_argument("-out", "--output", required=False, help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# inport txt file and convert each column to list
df_txt = pd.read_csv(args['coordinates'], header=None, sep="\t")
seq_start = df_txt.iloc[:,0].values.tolist()
seq_start[:] = [i - 1 for i in seq_start]
seq_end = df_txt.iloc[:,1].values.tolist()
# setup empty lists
headers = []
sequences = []
trimmed_records = []  
# choose fasta type to import
if args['type'] == 1:    
    # iterate for each record
    for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the lists
        headers.append(record.id)
        sequences.append(record.seq)
    # iterate all below lists in pairs
    for (a, b, c ,d) in zip(headers, sequences, seq_start, seq_end):
        trimmed_records.append(SeqRecord(Seq(str(b)[int(c):int(d)]), id='_'.join([str(a),str(c + 1),str(d)]), description=""))
    # export to fasta
    SeqIO.write(trimmed_records, args['output'], "fasta")
else:
    # import each fasta file from the working directory
    for filename in sorted(os.listdir(str(os.getcwd()))):
        if filename.endswith(".fa") or filename.endswith(".fasta"):
            # read each file
            record = SeqIO.read(filename, "fasta")
            # add this record to the lists
            headers.append(record.id)
            sequences.append(record.seq)
    # select directory to save the output files
    os.chdir(args['outdir'])
    # iterate all below lists in pairs
    for (a, b, c ,d) in zip(headers, sequences, seq_start, seq_end):
        trimmed_record = SeqRecord(Seq(str(b)[int(c):int(d)]), id='_'.join([str(a),str(c + 1),str(d)]), description="")
        # export to fasta
        SeqIO.write(trimmed_record, "".join([trimmed_record.id,".fasta"]), "fasta")
