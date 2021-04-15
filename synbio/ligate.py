# python3
import argparse
from Bio import SeqIO
import sys
# imput parameters
ap = argparse.ArgumentParser(description="ligate linear vector with DNA insert")
ap.add_argument("-vr", "--vector", required=True, help="linear vector(fasta format)")
ap.add_argument("-in", "--insert", required=True, help="sequence to insert in the vector(fasta format)")
ap.add_argument("-id", "--seqid", required=True, help="fasta header of the output file")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main 
# linear vector
for record in SeqIO.parse(args['vector'], "fasta"):
    x = str(record.seq)
# DNA insert
for record in SeqIO.parse(args['insert'], "fasta"):
    y = str(record.seq)
# merge
seqad = x + y
# output
sys.stdout = open(args['output'], 'a')
print(">"+args['seqid'], seqad, sep='\n')
sys.stdout.close()

