# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
import pandas as pd
# imput parameters
ap = argparse.ArgumentParser(description="ligate in pairs vectors in genbank format with annotations, with inserts in single-fasta files")
ap.add_argument("-txt", "--txt_file", required=False, help="input tab-seperated txt file with fasta and genbank filenames in each row(with extensions .gb, .gbk, .fa, .fasta and column names genbank and fasta respectively)")
args = vars(ap.parse_args())
# main
# inport txt file and convert each column to list
df_txt = pd.read_csv(args['txt_file'], sep="\t")
# create lists
gb_seqs = []
fasta_seqs = []
fasta_ids = []
gb_ids = []
gb_features = []
# linear vectors
# import each genbank file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".gb") or filename.endswith(".gbk"):
        plasmid = SeqIO.read(filename, "genbank")
        gb_seqs.append(str(plasmid.seq))
        gb_features.append(plasmid.features)
        gb_ids.append(str(filename))
# create dataframe and add the lists on it
df_gb = pd.DataFrame()
df_gb['genbank'] = gb_ids
df_gb['genbank_seqs'] = gb_seqs
df_gb['genbank_features'] = gb_features
# DNA insert
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        record = SeqIO.read(filename, "fasta")
        fasta_seqs.append(str(record.seq))
        fasta_ids.append(str(filename))
# create dataframe and add the lists on it
df_fa = pd.DataFrame()
df_fa['fasta'] = fasta_ids
df_gb['fasta_seqs'] = fasta_seqs
# merge data frames
df_full = df_txt.join(df_gb.set_index('genbank'), on='genbank')
df_full = df_full.join(df_fa.set_index('fasta'), on='fasta')
# convert to list
gb_list = df_full.iloc[:,0].values.tolist()
fasta_list = df_full.iloc[:,1].values.tolist()
genbank_sequences = df_full.iloc[:,2].values.tolist()
genbank_features = df_full.iloc[:,3].values.tolist()
fasta_sequences = df_full.iloc[:,4].values.tolist()
# iterate all below lists in pairs
for (a,b,c,d,e) in zip(gb_list,fasta_list,genbank_sequences,genbank_features,fasta_sequences):
    # merge
    seqad = str(c) + str(e)
    # add this record to the list
    ligated = SeqRecord(Seq(seqad),id='_'.join([str(a).split(".")[0], str(b).split(".")[0]]),description="",annotations={"molecule_type":"DNA","topology":"circular"})
    ligated.features = d
    # export to genbank
    SeqIO.write(ligated,"".join([str(a).split(".")[0],"_",str(b).split(".")[0],".gb"]), "genbank")
