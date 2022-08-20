# python 3
import os
import argparse 
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser(description="count number of fasta sequences for each fasta file in the current working directory by indexing the  multi-fasta files")
ap.add_argument("-out", "--output", required=True, help="output tab seperated 2-column txt file with fasta filenames and number of fasta sequences. file extensions that are supported: .fasta, .fa, .fna, .faa, .fsa, .ffn, frn, .mpfa")
args = vars(ap.parse_args())
# create fasta index for each fasta file
with open(args['output'], 'a') as filehandle:
    for filename in sorted(os.listdir(os.getcwd())):
        if filename.endswith(".fa") or filename.endswith(".fasta") or filename.endswith(".fna") or filename.endswith(".faa") or filename.endswith(".fsa") or filename.endswith(".ffn") or filename.endswith(".frn") or filename.endswith(".mpfa"):
            features = Fasta(filename)
            filehandle.write('%s\n' % '\t'.join([filename,str(len(features.keys()))]))
            del features


