# python3
import argparse
import itertools
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
# imput parameters
ap = argparse.ArgumentParser(description="ligate linear vector with DNA insert by pair from each input multi-fasta file")
ap.add_argument("-vr", "--vector", required=True, help="linear vectors (multi-fasta file the order is important as the 1st vector matches the 1st insert in the file etc)")
ap.add_argument("-in", "--insert", required=True, help="sequences to insert in the vectors (multi-fasta file the order is important as the 1st insert matches the 1st vector in the file etc)")
ap.add_argument("-out", "--output", required=True, help="output genbank file with circular sequences")
args = vars(ap.parse_args())
# main 
# linear vector
output_handle = open(args['output'], "w")
 # setup empty lists
plasmid_seqs = []
plasmid_ids = []
# select all plasmid sequences and ids to seperate lists
for plasmid in SeqIO.parse(args['vector'], "fasta"):
    plasmid_seqs.append(plasmid.seq)
    plasmid_ids.append(plasmid.id)
# DNA insert
insert_ids = []
insert_seqs = []
for record in SeqIO.parse(args['insert'], "fasta"):
    insert_seqs.append(record.seq)
    insert_ids.append(record.id)
# iter all element of the lists by groups of 4 variables
records = []
for (a, b, c, d) in itertools.zip_longest(plasmid_ids, plasmid_seqs, insert_ids, insert_seqs):
    # merge
    seqad = str(d) + str(b)
        # add this record to the list
    records.append(SeqRecord(Seq(seqad,generic_dna),id='_'.join([str(c),str(a)]),description="",annotations={"topology":"circular"}))
# export to fasta
SeqIO.write(records,output_handle, "genbank")
output_handle.close()
