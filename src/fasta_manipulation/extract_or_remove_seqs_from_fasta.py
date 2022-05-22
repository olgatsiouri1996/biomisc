# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-out", "--output", required=False, help="output fasta file")
ap.add_argument("-pro", "--program",type=int, default=1, required=False, help="choose to exract or remove( 1) extract, 2) remove, 3) extract and export as single-fasta files, 4) remove and export as single-fasta files. Defaults to 1)")
ap.add_argument("-headers", "--headers", required=True, help="file with fasta headers to retrieve the output fasta sequences")
ap.add_argument("-dir", "--directory", required=False, type=str, default='.', help="relative or absolute path to the output directory to save the single-fasta files. Default is the current directory")
args = vars(ap.parse_args())
# main
wanted = set()
with open(args['headers']) as f:
    for line in f:
        line = line.strip()
        if line != "":
            wanted.add(line)
# choose program
program = args['program']
# extract            
if program == 1:
    fasta_sequences = SeqIO.parse(open(args['input']),'fasta')
    with open(args['output'], "w") as f:
        for seq in fasta_sequences:
            if seq.id in wanted:
                SeqIO.write([seq], f, "fasta")
# remove
if program == 2:
    fasta_sequences = SeqIO.parse(open(args['input']),'fasta')
    with open(args['output'], "w") as f:
        for seq in fasta_sequences:
            if seq.id not in wanted:
                SeqIO.write([seq], f, "fasta")
# extract and export as single-fasta files
if program == 3:
    records = []
    fasta_sequences = SeqIO.parse(open(args['input']),'fasta')
    os.chdir(args['directory'])
    for seq in fasta_sequences:
        if seq.id in wanted:
            SeqIO.write(seq, "".join([str(seq.id),".fasta"]), "fasta")
# remove and export as single-fasta files
if program == 4:
    records = []
    fasta_sequences = SeqIO.parse(open(args['input']),'fasta')
    os.chdir(args['directory'])
    for seq in fasta_sequences:
        if seq.id not in wanted:
            SeqIO.write(seq, "".join([str(seq.id),".fasta"]), "fasta")
