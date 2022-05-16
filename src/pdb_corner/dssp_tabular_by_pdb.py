# python3
import os
from Bio.PDB import *
import pandas as pd
import warnings
from Bio import BiopythonWarning
# main
# ignore warnings
warnings.simplefilter('ignore', BiopythonWarning)
# retrieves each pdb file on the current directory and calculates the secondary structure percentage
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".pdb"):
        # retrieve pdb id
        pdbid = filename.split('.')[0]
        # select model
        parser = PDBParser()
        s = parser.get_structure("name", filename)
        fill = s[0]
        dssp = DSSP(fill, filename, dssp='mkdssp')
        df = pd.DataFrame(dssp)
        df = df.loc[:, [0,1,2]]
        # export
        with open(''.join([pdbid,".txt"]), 'a') as f:
            f.write(
                df.to_csv(header = ['residue_number','residue_name', 'residue_structure'], index = False, sep= "\t", doublequote= False, line_terminator= '\n')
            )
        del dssp ; del df