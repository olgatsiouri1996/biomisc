# python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
# imput parameters
ap = argparse.ArgumentParser(description="ligate vector with insert")
ap.add_argument("-vr", "--vector", required=True, help="vector in genbank format")
ap.add_argument("-in", "--insert", required=True, help="sequence to insert in the vector in fasta format")
ap.add_argument("-out", "--output", required=True, help="output genbank file with circular sequence")
args = vars(ap.parse_args())
# main 
# linear vector
plasmid = SeqIO.read(args['vector'], "genbank")
x = str(plasmid.seq)
# DNA insert
record = SeqIO.read(args['insert'], "fasta")
y = str(record.seq)
# merge
seqad = x + y
# add this record to the list
ligated = SeqRecord(Seq(seqad),id='_'.join([record.id,args['vector'].split(".")[0]]),description="",annotations={ "molecule_type":"DNA","topology":"circular"})
ligated.features = plasmid.features
# export to genbank
SeqIO.write(ligated,args['output'], "genbank")
