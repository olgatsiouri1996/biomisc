# python3
import argparse
from Bio import SeqIO
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-gb", "--genbank", required=True, help="input genbank file")
ap.add_argument("-fa","--fasta", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
count = SeqIO.convert(args['genbank'], "genbank", args['fasta'], "fasta")
