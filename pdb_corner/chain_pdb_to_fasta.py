# python3
import argparse
from Bio.PDB import *
import sys
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-pdb", "--input_pdb", required=True, help="input pdb file")
ap.add_argument("-model", "--pdb_model", required=True, help="model from pdb file to select(integer)")
ap.add_argument("-chain", "--pdb_chain", required=True, help="chain from pdb file to select")
ap.add_argument("-id", "--pdb_id", required=True, help="pdb id of the protein structure")
ap.add_argument("-fasta", "--fasta_file", required=True, help="output fasta file")
args = vars(ap.parse_args())
#main
def seq_from_pdb(structure):
    ppb = PPBuilder()
    for pp in ppb.build_peptides(structure):
        print(">"+args['pdb_id']+"_"+args['pdb_chain'],pp.get_sequence(), sep="\n")

parser = PDBParser()
s = parser.get_structure("name", args['input_pdb'])
fill = s[int(args['pdb_model'])][args['pdb_chain']]
sys.stdout = open(args['fasta_file'], 'a')
seq_from_pdb(fill)
sys.stdout.close()
