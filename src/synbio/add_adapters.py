# python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,  help="input single or multi fasta file")
ap.add_argument("-l", "--left", required=False, type=str, default="",  help="adapter to the left of the sequence. Default is no left adapter sequence to add")
ap.add_argument("-r", "--right", required=False, type=str, default="",  help="adapter to the right of the sequence. Default is no right adapter sequence to add")
ap.add_argument("-o", "--output", required=True,  help="output fasta file")
args = vars(ap.parse_args())
# main
records = [] # setup an empty list
for record in SeqIO.parse(args['input'], "fasta"):
    # add this record to the list
    records.append(SeqRecord(Seq(''.join([args['left'],str(record.seq),args['right']])),id=record.id,description=record.description))
# export to fasta
SeqIO.write(records, args['output'], "fasta")
