# python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
# imput parameters
ap = argparse.ArgumentParser(description="ligate linear vector with DNA insert")
ap.add_argument("-vr", "--vector", required=True, help="linear vector/s (single or multi fasta file)")
ap.add_argument("-in", "--insert", required=True, help="sequence/s to insert in the vector(single or multi fasta file)")
ap.add_argument("-out", "--output", required=True, help="output genbank file with circular sequence/s")
args = vars(ap.parse_args())
# main 
# linear vector
output_handle = open(args['output'], "w")
records = [] # setup an empty list
for plasmid in SeqIO.parse(args['vector'], "fasta"):
    x = str(plasmid.seq)
    # DNA insert
    for record in SeqIO.parse(args['insert'], "fasta"):
        y = str(record.seq)
    # merge
        seqad = y + x
        # add this record to the list
        records.append(SeqRecord(Seq(seqad,generic_dna),id='_'.join([record.id,plasmid.id]),description="",annotations={"topology":"circular"}))
# export to fasta
SeqIO.write(records,output_handle, "genbank")
output_handle.close()
