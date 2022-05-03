# python3
import os
import argparse
import Bio
from Bio.PDB import *
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input pdb file with 1 model")
ap.add_argument("-dir", "--directory", required=False, default='.', help=" directory to save output pdb file(relative path)")
args = vars(ap.parse_args())
# main
# retrieve pdb id
pdbid = args['input_file'].split('.')[0]
# import pdb
parser = PDBParser()
s = parser.get_structure("name", args['input_file'])
model = s[0]
# change output directory
os.chdir(os.path.realpath(args['directory']))
for chain in model:
	io = PDBIO()
	io.set_structure(chain)
	io.save(''.join([pdbid,"_",chain.get_id(),".pdb"]))
