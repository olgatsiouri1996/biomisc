# python3
import argparse
from Bio import SeqIO
from Bio.Alphabet import generic_dna, generic_protein
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa","--fasta", required=True, help="input fasta file")
ap.add_argument("-gb", "--genbank", required=True, help="output genbank file")
args = vars(ap.parse_args())
# main
input_handle = open(args['fasta'], "rU")
output_handle = open(args['genbank'], "w")
# import fasta
sequences = list(SeqIO.parse(input_handle, "fasta"))

# asign generic_dna or generic_protein
for seq in sequences:
    seq.seq.alphabet = generic_dna
# output
count = SeqIO.write(sequences, output_handle, "genbank")

output_handle.close()
input_handle.close()

        
