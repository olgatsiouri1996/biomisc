# python3
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-mfa", "--multifasta", required=True,  help="input multi-fasta file to merge its sequences")
ap.add_argument("-id", "--seqid", required=True, type=str, help="fasta header of the output file")
ap.add_argument("-sp", "--spacer", required=False, type=str, default="", help="nucleotides or aminoacids to add between the merged fasta sequences. Default: no sequence to add")
ap.add_argument("-sfa", "--singlefasta", required=True,  help="output single-fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
for record in SeqIO.parse(args['multifasta'], "fasta"):
	sequences.append(record.seq)
# merge all sequences at 1 and create SeqRecord object
merged_seqs = SeqRecord(Seq(args['spacer'].join(map(str,sequences))),id=args['seqid'],description="")
# export to fasta
SeqIO.write(merged_seqs, args['singlefasta'], "fasta")
