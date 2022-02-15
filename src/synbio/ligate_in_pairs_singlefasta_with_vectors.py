# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
import  pandas as pd
# imput parameters
ap = argparse.ArgumentParser(description="ligate in pairs vectors in genbank format with annotations, with inserts in single-fasta files")
ap.add_argument("-txt", "--txt_file", required=False, help="input 2-column tab-seperated txt file with genbank and fasta filenames respectively in each row(with extensions .gb, .gbk, .fa, .fasta )")
args = vars(ap.parse_args())
# main
# inport txt file and convert each column to list
df_txt = pd.read_csv(args['txt_file'], header=None, sep="\t")
gb_list = df_txt.iloc[:,0].values.tolist()
fasta_list = df_txt.iloc[:,1].values.tolist()
# create lists
gb_seqs = []
fasta_seqs = []
gb_features = []
# linear vectors
# import each genbank file from the list
for i in gb_list:
    plasmid = SeqIO.read(i, "genbank")
    gb_seqs.append(str(plasmid.seq))
    gb_features.append(plasmid.features)
# DNA insert
# import each fasta file from the list
for i in fasta_list:
    record = SeqIO.read(i, "fasta")
    fasta_seqs.append(str(record.seq))
# iterate all below lists in pairs
for (a,b,c,d,e) in zip(gb_list,fasta_list,gb_seqs,gb_features,fasta_seqs):
    # merge
    seqad = str(c) + str(e)
    # add this record to the list
    ligated = SeqRecord(Seq(seqad),id='_'.join([str(a).split(".")[0], str(b).split(".")[0]]),description="",annotations={"molecule_type":"DNA","topology":"circular"})
    ligated.features = d
    # export to genbank
    SeqIO.write(ligated,"".join([str(a).split(".")[0],"_",str(b).split(".")[0],".gb"]), "genbank")
