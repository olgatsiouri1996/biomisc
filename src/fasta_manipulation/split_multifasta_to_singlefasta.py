# python3
import os
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-mfa", "--multifasta", required=True,  help="input multi-fasta file to split to single-fasta")
ap.add_argument("-dir", "--directory", required=False, default='.', type=str, help="output directory to save the single-fasta files. Default is the current directory")
args = vars(ap.parse_args())
# main
# set working directory
records = SeqIO.parse(args['multifasta'], "fasta")
os.chdir(args['directory'])
for record in records:
	SeqIO.write(record, ''.join([record.id,".fasta"]), "fasta")
