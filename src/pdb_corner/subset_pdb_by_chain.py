# python3
import argparse
import Bio
from Bio.PDB import *
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input pdb file with 1 model")
ap.add_argument("-chain", "--pdb_chain", required=True, help="chain from pdb file to select")
ap.add_argument("-out", "--output_file", required=True, help="output pdb file")
args = vars(ap.parse_args())
# main
parser = PDBParser()
s = parser.get_structure("name", args['input_file'])
model = s[0]
chain = model[args['pdb_chain']]
io = PDBIO()
io.set_structure(chain)
io.save(args['output_file'])
