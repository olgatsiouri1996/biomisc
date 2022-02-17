# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
# imput parameters
ap = argparse.ArgumentParser(description="ligate vectors in genbank format with annotations, with inserts in a multi-fasta file")
ap.add_argument("-fasta", "--multi_fasta", required=False, help="multi-fasta file to inport")
args = vars(ap.parse_args())
# main 
# linear vectors
# import each genbank file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".gb") or filename.endswith(".gbk"): 
        plasmid = SeqIO.read(filename, "genbank")
        x = str(plasmid.seq)
        gb_file = filename.split(".")[0]
        # DNA insert
        # import each fasta file from the working directory
        for record in SeqIO.parse(args['multi_fasta'],"fasta"):
            y = str(record.seq)
            # merge
            seqad = x + y
             # add this record to the list
            ligated = SeqRecord(Seq(seqad),id='_'.join([record.id,gb_file]),description="",annotations={"molecule_type":"DNA","topology":"circular"})
            ligated.features = plasmid.features
            # export to genbank
            SeqIO.write(ligated,"".join([record.id,"_",gb_file,".gb"]), "genbank")
