# python3
import os
import argparse
import Bio
from Bio.PDB import *
import  pandas as pd
import warnings
from Bio import BiopythonWarning
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-pdb", "--pdbdir", required=False, type=str, default='.', help=" directory containing the input pdb files(absolute path). Defaults to the current directory")
ap.add_argument("-txt", "--txtfile", required=True, help="4 column tabular txt file with pdb filename, chain, start and end position columns respectively")
ap.add_argument("-out", "--outdir", required=False, type=str, default='.', help=" directory to save the output pdb files(absolute path). Defaults to the current directory")
args = vars(ap.parse_args())
# main
# ignore warnings
warnings.simplefilter('ignore', BiopythonWarning)
# inport txt file and convert each column to list
df_txt = pd.read_csv(args['txtfile'], header=None, sep="\t")
ids = df_txt.iloc[:,0].values.tolist()
chains = df_txt.iloc[:,1].values.tolist()
star_pos = df_txt.iloc[:,2].values.tolist()
end_pos = df_txt.iloc[:,3].values.tolist()	
# iterate all above lists and subset each pdb file
for (a, b, c, d) in zip(ids,chains,star_pos,end_pos):
# set working directory
	os.chdir(args['pdbdir'])
# import pdb
	parser = PDBParser()
	s = parser.get_structure("name", ''.join([str(a),".pdb"]))
# set working directory to export
	os.chdir(args['outdir'])
# supbset and export to pdb
	Bio.PDB.Dice.extract(s, str(b), int(c), int(d), ''.join([str(a),"_",str(b),"_",str(c),"_",str(d),".pdb"]))

