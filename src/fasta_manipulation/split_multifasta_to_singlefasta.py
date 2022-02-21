# python3
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-mfa", "--multifasta", required=True,  help="input multi-fasta file to split to single-fasta")
args = vars(ap.parse_args())
# main
for record in SeqIO.parse(args['multifasta'], "fasta"):
	one_seq = SeqRecord(Seq(record.seq),id=record.id,description="")
	SeqIO.write(one_seq, ''.join([record.id,".fasta"]), "fasta")
