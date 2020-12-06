# python3
import argparse
from Bio.PDB import *
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_pdb", required=True, help="input pdb file")
ap.add_argument("-model", "--pdb_model", required=False, default= 0, help="model from pdb file to select(integer, default=0)")
ap.add_argument("-chain", "--pdb_chain", required=True, help="chain from pdb file to select")
ap.add_argument("-out", "--output_pdb", required=True, help="output pdb file")
args = vars(ap.parse_args())
# main
parser = PDBParser()
s = parser.get_structure("name", args['input_pdb'])
fill = s[int(args['pdb_model'])][args['pdb_chain']]
io = PDBIO()
io.set_structure(fill)
io.save(args['output_pdb'])