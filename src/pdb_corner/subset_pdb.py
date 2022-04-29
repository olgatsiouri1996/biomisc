# python3
import argparse
import Bio
from Bio.PDB import *
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input pdb file")
ap.add_argument("-chain", "--pdb_chain", required=True, help="chain from pdb file to select")
ap.add_argument("-start", "--chain_start", required=True, type=int, help="amino acid in chain to start writing the pdb file")
ap.add_argument("-end", "--chain_end", required=True, type=int, help="amino acid in chain to end writing the pdb file")
args = vars(ap.parse_args())
#main
parser = PDBParser()
s = parser.get_structure("name", args['input_file'])
Bio.PDB.Dice.extract(s, args['pdb_chain'], args['chain_start'],args['chain_end'], ''.join([args['input_file'].split(".")[0],"_",args['pdb_chain'],"_",str(args['chain_start']),"_",str(args['chain_end']),".pdb"]))

