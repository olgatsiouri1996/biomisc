# python3
import argparse
import itertools
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-up", "--upstream", required=True,  help="upstream adapters(fasta format)")
ap.add_argument("-fa", "--fasta", required=True,  help="input single or multi fasta  file with the sequence/s to add adapters")
ap.add_argument("-down", "--downstream", required=True,  help="downstream adapters(fasta format)")
ap.add_argument("-out", "--output", required=True,  help="output fasta file")
args = vars(ap.parse_args())
# main
# first adapter
forw = [] # setup an empty list
for record in SeqIO.parse(args['upstream'], "fasta"):
    forw.append(record.seq)
# second adapter
rever = [] # setup an empty list
for record in SeqIO.parse(args['upstream'], "fasta"):
    rever.append(record.seq)
# sequence
records = []
headers = [] # setup empty lists
for record in SeqIO.parse(args['fasta'], "fasta"):
    records.append(record.seq)
    headers.append(record.id)
# setup an empty list
added_seqs = [] 
# iterate for 4 items of each list
for (a, b, c, d) in itertools.zip_longest(forw, records, rever, headers):
# merge
    seqad = str(a) + str(b) + str(c) 
    # add this record to the list
    added_seqs.append(SeqRecord(Seq(seqad),id=str(d),description=""))
# export to fasta
SeqIO.write(added_seqs, args['output'], "fasta")
