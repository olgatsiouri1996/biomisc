# python3
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input pdb file without SEQRES header(you should add a header if you want your output fasta file to have one otherwise ?? apears on the fasta header line)")
ap.add_argument("-out", "--output_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
count = SeqIO.convert(args['input_file'], "pdb-atom", args['output_file'], "fasta")
