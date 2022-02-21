# python3
import argparse
import os
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa", "--multifasta", required=True,  help="output multi-fasta file")
args = vars(ap.parse_args())
# main
# creat list
records = []
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        record = SeqIO.read(filename, "fasta")
        records.append(record)
# export all SeqRecords to a multi-fasta file
SeqIO.write(records,args['multifasta'], "fasta")
