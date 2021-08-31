#python3
import argparse
import os
from Bio.PDB import *
import pandas as pd
# input parameters
ap = argparse.ArgumentParser(description="search for pdb files in the current directory, run DSSP, calculate the percentage of secondary structures for each pdb and export a txt file with the file names as rows and the secondary structure as columns")
ap.add_argument("-out", "--output", required=True, help="output txt file")
args = vars(ap.parse_args())
# retrieve fasta file names
file_list = []
for filename in os.listdir(str(os.getcwd())):
    if filename.endswith(".pdb"):
        file_list.append(filename.split(".pdb")[0])
# main
df_list = []  # setup empty list
# retrieves each pdb file on the current directory and calculates the secondary structure percentage
for filename in os.listdir(str(os.getcwd())):
    if filename.endswith(".pdb"):
        parser = PDBParser()
        s = parser.get_structure("name", filename)
        fill = s[0]
        dssp = DSSP(fill, filename, dssp='mkdssp')
        df = pd.DataFrame(dssp)
        df = df.loc[:, 2]
        struct_list = df.values.tolist()
        df1 = pd.DataFrame()
        df1['struct_list'] = struct_list
        df1 = df1['struct_list'].value_counts()
        df1 = round((df1 / df1.sum(axis=0)) * 100, 2)
        df_list.append(df1)
        del df
        struct_list.clear()
        del df1
# concatenate all dataframes into 1
stats = pd.concat(df_list,axis=1)
stats.columns = file_list
stats = stats.fillna(stats)
# convert rows to columns
stats_t = stats.T
# export
with open(args['output'], 'a') as f:
    f.write(
        stats_t.to_csv(header = True, index = True, sep= "\t", doublequote= False, line_terminator= '\n')
    )
