# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-up", "--upstream", required=True,  help="upstream adapter(fasta format)")
ap.add_argument("-down", "--downstream", required=True,  help="downstream adapter(fasta format)")
args = vars(ap.parse_args())
# main
# first adapter
x = SeqIO.read(args['upstream'], "fasta")
# second adapter
z = SeqIO.read(args['downstream'], "fasta")
# sequence
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        y = SeqIO.read(filename, "fasta")
        # merge
        seqad = str(x.seq) + str(y.seq) + str(z.seq)
            # create SeqRecord
        record = SeqRecord(Seq(seqad),id=y.id,description="")
        # export to fasta
        SeqIO.write(record, "".join([filename.split(".")[0],"_","with","_","ad",".fasta"]), "fasta")
