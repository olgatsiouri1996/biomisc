#python3
import argparse
from Bio.PDB import *
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-pdb", "--input_pdb", required=True, help="input pdb file")
ap.add_argument("-model", "--pdb_model", required=False, default= 0, help="model from pdb file to select(integer, default=0)")
ap.add_argument("-out", "--output", required=True, help="output txt file")
args = vars(ap.parse_args())
# main
parser = PDBParser()
s = parser.get_structure("name", args['input_pdb'])
fill = s[int(args['pdb_model'])]
dssp = DSSP(fill, args['input_pdb'], dssp='mkdssp')
df = pd.DataFrame(dssp)
df = df.loc[:, [0,1,2]]
# export
with open(args['output'], 'a') as f:
    f.write(
        df.to_csv(header = ['residue_number','residue_name', 'residue_structure'], index = False, sep= "\t", doublequote= False, line_terminator= '\n')
    )
