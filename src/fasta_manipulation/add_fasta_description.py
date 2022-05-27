# python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="input single or multi fasta file")
ap.add_argument("-d", "--descriptions", required=True, help="input 1-column txt file with fasta_descriptions")
ap.add_argument("-o", "--output", required=True,  help="output fasta file")
args = vars(ap.parse_args())
# main
# import file with fasta descriptions
with open(args['descriptions'], 'r') as f:
    fasta_descriptions = f.readlines()
fasta_descriptions = [x.strip() for x in fasta_descriptions]
records_with_fasta_descriptions = [] # setup an empty list
records = SeqIO.parse(args['input'], "fasta")
# iterate using the above lists
for (record, fasta_description) in zip(records, fasta_descriptions):
    record.description = str(fasta_description)
    records_with_fasta_descriptions.append(record)
# export to fasta
SeqIO.write(records_with_fasta_descriptions, args['output'], "fasta")
