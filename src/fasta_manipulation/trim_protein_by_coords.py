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
ap.add_argument("-coords", "--coordinates", required=True, help="input 3-column tab-seperated txt file with id, start and end positions respectively in each row")
ap.add_argument("-type", "--type", required=False,default=1, type=int, help="type of fasta to import 1) 1 multi-fasta file 2)  many single-fasta files. Default is 1")
ap.add_argument("-outdir", "--outdir", required=False, type=str, default='.', help="directory to save output fasta files")
ap.add_argument("-out", "--output", required=False, help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# inport txt file and convert each column to list
df_txt = pd.read_csv(args['coordinates'], header=None, sep="\t")
ids = df_txt.iloc[:,0].values.tolist()
seq_start = df_txt.iloc[:,1].values.tolist()
seq_start[:] = [i - 1 for i in seq_start]
seq_end = df_txt.iloc[:,2].values.tolist()
# setup empty lists
records = []
trimmed_records = []
# choose fasta type to import
if args['type'] == 1:    
    # iterate for each record
    for i in ids:
        for record in SeqIO.parse(args['input'], "fasta"):
            if i == record.id:
                records.append(record)
    # iterate all below lists in pairs
    for (a, b, c) in zip(records, seq_start, seq_end):
        trimmed_records.append(SeqRecord(Seq(str(a.seq)[int(b):int(c)]), id='_'.join([str(a.id),str(b + 1),str(c)]), description=""))
    # export to fasta
    SeqIO.write(trimmed_records, args['output'], "fasta")
else:
    # import each fasta file from the working directory
    os.chdir(str(os.getcwd()))
    for i in ids:
        # read each file
        record = SeqIO.read(''.join([i,".fasta"]), "fasta")
        # add this record to the lists
        records.append(record)
    # select directory to save the output files
    os.chdir(args['outdir'])
    # iterate all below lists in pairs
    for (a, b, c) in zip(records, seq_start, seq_end):
        trimmed_record = SeqRecord(Seq(str(a.seq)[int(b):int(c)]), id='_'.join([str(a.id),str(b + 1),str(c)]), description="")
        # export to fasta
        SeqIO.write(trimmed_record, "".join([trimmed_record.id,".fasta"]), "fasta")
