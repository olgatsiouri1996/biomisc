# python3
import argparse
from Bio.PDB import *
import pandas as pd
import os
# input paramexters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input pdb file(every name except: out.pdb)")
ap.add_argument("-model", "--model", required=False, default= 0, help="model from pdb file to select(integer, default=0)")
ap.add_argument("-chain", "--chain", required=True, help="chain from pdb file to select")
ap.add_argument("-start", "--start", required=False, type=int, help="amino acid in chain to start writing the pdb file")
ap.add_argument("-end", "--end", required=False, type=int, help="amino acid in chain to end writing the pdb file")
ap.add_argument("-pro", "--program", required=False, type=int, default=1, help="program to choose: 1. select only the model and chain, 2. select model, chain, start and end locations. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output txt file(every name except: out.pdb)")
args = vars(ap.parse_args())
# main
# select model and chain
parser = PDBParser()
s = parser.get_structure("name", args['input'])
fill = s[int(args['model'])][args['chain']]
io = PDBIO()
io.set_structure(fill)
io.save("out.pdb")
# import trimed pdb file and run dssp 
parser = PDBParser()
s = parser.get_structure("name", "out.pdb")
fill = s[0]
dssp = DSSP(fill,"out.pdb", dssp='mkdssp')
df = pd.DataFrame(dssp)
df = df.loc[:, 2]
# choose program
if args['program'] == 1:
    pass    
else:
    df = df.loc[int(args['start'] -1):int(args['end'] -1)]
# create list with structures
struct_list = df.values.tolist()
df1 = pd.DataFrame()
df1['struct_list'] = struct_list
df1 = df1['struct_list'].value_counts()
df1 = round((df1 / df1.sum(axis=0)) * 100, 2)
# export
with open(args['output'], 'a') as f:
    f.write(
        df1.to_csv(header = False, index = True, sep= "\t", doublequote= False, line_terminator= '\n')
    )
# remove intermediate file
os.system("rm *out.pdb")
