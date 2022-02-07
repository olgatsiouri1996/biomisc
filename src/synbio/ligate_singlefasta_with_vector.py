# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
# imput parameters
ap = argparse.ArgumentParser(description="ligate vector with inserts in single-fasta files")
ap.add_argument("-vr", "--vector", required=True, help="vector in genbank format")
args = vars(ap.parse_args())
# main 
# linear vector
plasmid = SeqIO.read(args['vector'], "genbank")
x = str(plasmid.seq)
# DNA insert
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        record = SeqIO.read(filename, "fasta")
        y = str(record.seq)
        # merge
        seqad = x + y
        # add this record to the list
        ligated = SeqRecord(Seq(seqad),id='_'.join([record.id,args['vector'].split(".")[0]]),description="",annotations={"molecule_type":"DNA","topology":"circular"})
        ligated.features = plasmid.features
        # export to genbank
        SeqIO.write(ligated,"".join([filename.split(".")[0],"_",args['vector'].split(".")[0],".gb"]), "genbank")
