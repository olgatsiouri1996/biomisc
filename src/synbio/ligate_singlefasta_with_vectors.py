# python3
import os
import warnings
from Bio import BiopythonWarning
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
# imput parameters
ap = argparse.ArgumentParser(description="ligate vectors in genbank format with annotations, with inserts in single-fasta files")
ap.add_argument("-dir", "--directory", required=False,default='.', help="directory to export the output genbank files. Default is the current directory")
args = vars(ap.parse_args())
# main 
# remove warnings
warnings.simplefilter('ignore',BiopythonWarning)
# add final list
final_gbs = []
# linear vectors
# import each genbank file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".gb") or filename.endswith(".gbk"): 
        plasmid = SeqIO.read(filename, "genbank")
        x = str(plasmid.seq)
        gb_file = filename.split(".")[0]
        # DNA insert
        # import each fasta file from the working directory
        for filename in sorted(os.listdir(str(os.getcwd()))):
            if filename.endswith(".fa") or filename.endswith(".fasta"):
                record = SeqIO.read(filename, "fasta")
                y = str(record.seq)
                # merge
                seqad = x + y
                # add this record to the list
                ligated = SeqRecord(Seq(seqad),id='_'.join([record.id,gb_file]),description="",annotations={"molecule_type":"DNA","topology":"circular"})
                ligated.features = plasmid.features
                final_gbs.append(ligated)
# select output directory
os.chdir(args['directory'])
# export to genbank
for final_gb in final_gbs:
    SeqIO.write(final_gb,"".join([final_gb.id,".gb"]), "genbank")
