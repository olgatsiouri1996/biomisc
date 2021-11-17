# python3
import argparse
from Bio.PDB import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-pdb", "--pdb", required=True, help="input pdb file")
ap.add_argument("-model", "--model",default=0, required=False, help="model from pdb file to select(integer). Default is 0(1 model only)")
ap.add_argument("-chain", "--chain", required=True, help="chain from pdb file to select")
args = vars(ap.parse_args())
# main
# select chain
parser = PDBParser()
s = parser.get_structure("name", args['pdb'])
fill = s[int(args['model'])][args['chain']]
# retrieve the pdb id of the input file
pdb_id = str(args['pdb']).split(".")[0]
# export to fasta
ppb = PPBuilder()
for pp in ppb.build_peptides(fill):
    record = SeqRecord(Seq(str(pp.get_sequence())),id="".join([str(pdb_id),"_",str(args['chain'])]),description="")
    SeqIO.write(record, "".join([str(pdb_id),"_",str(args['chain']),".fasta"]), "fasta")

