# python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# imput parameters
ap = argparse.ArgumentParser(description="ligate linear vector with DNA insert")
ap.add_argument("-vr", "--vector", required=True, help="linear vector(fasta format)")
ap.add_argument("-in", "--insert", required=True, help="sequence/s to insert in the vector(single or multi fasta file)")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main 
# linear vector
for record in SeqIO.parse(args['vector'], "fasta"):
    x = str(record.seq)
# DNA insert
records = [] # setup an empty list
for record in SeqIO.parse(args['insert'], "fasta"):
    y = str(record.seq)
# merge
    seqad = x + y
    # add this record to the list
    records.append(SeqRecord(Seq(seqad),id=record.id,description=""))
# export to fasta
SeqIO.write(records, args['output'], "fasta")
