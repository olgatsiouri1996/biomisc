# python3
import argparse
from Bio import SeqIO
from synbiopython.codon import table, taxonomy_utils, utils
import sys
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True,  help="input multi or single fasta file")
ap.add_argument("-taxid", "--taxid", required=True, help="taxonomy id to retrieve the codon table for optimization")
ap.add_argument("-out", "--output", required=True,  help="output single or multi fasta file")
args = vars(ap.parse_args())
# main
    name = taxonomy_utils.get_organism_name(args['taxid'])
    name_table = table.get_table(name)
# output
sys.stdout = open(args['input'], 'a')
for record in SeqIO.parse(args['output'], "fasta"):
    print(">"+record.id,utils.optimise(name_table, str(record.seq)), sep='\n')
sys.stdout.close()

