# python3
from gooey import *
from Bio.PDB import *
from biopandas.pdb import PandasPdb
import os
#import pandas as pd
# input parameters
@Gooey(required_cols=3, program_name='subset pdb by chain', header_bg_color= '#DCDCDC', terminal_font_color= '#DCDCDC', terminal_panel_color= '#DCDCDC')
def main():
    ap = GooeyParser(description="subsets a pdb file by selecting the model and chain from it(does residue renumbering)")
    ap.add_argument("-in", "--input_pdb", required=True, widget='FileChooser', help="input pdb file")
    ap.add_argument("-model", "--pdb_model", required=False, default= 0, help="model from pdb file to select(integer, default=0)")
    ap.add_argument("-chain", "--pdb_chain", required=True, help="chain from pdb file to select")
    ap.add_argument("-out", "--output_pdb", required=True, widget='FileSaver', help="output pdb file")
    args = vars(ap.parse_args())
    # import pdb
    parser = PDBParser()
    s = parser.get_structure("name", args['input_pdb'])
    fill = s[int(args['pdb_model'])][args['pdb_chain']]
    io = PDBIO()
    io.set_structure(fill)
    io.save("subset_out.pdb")
    # main
    ppdb = PandasPdb()
    ppdb.read_pdb('subset_out.pdb')
    ppdb.df['ATOM']
    ppdb.df['ATOM']['residue_number'] = ppdb.df['ATOM']['residue_number'] - ppdb.df['ATOM']['residue_number'].min() +1
    ppdb.to_pdb(path='renumb_out.pdb', 
                records=['ATOM'], 
                gz=False, 
                append_newline=True)
    # export
    parser = PDBParser()
    s = parser.get_structure("name", "renumb_out.pdb")
    io = PDBIO()
    io.set_structure(s)
    io.save(args['output_pdb'])
    os.system("del *out.pdb")

if __name__ == '__main__':
    main()