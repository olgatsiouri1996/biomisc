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
ap.add_argument("-start", "--start", required=False,default=1, type=int, help="amino acid in chain to start writing the fasta file. Default is 1")
ap.add_argument("-end", "--end", required=False, type=int, help="amino acid in chain to end writing the fasta file")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose 1) add both start and end location 2) the end location with be that of the latest amino acid in the chain. Default is 1")
args = vars(ap.parse_args())
# main
# select chain
parser = PDBParser()
s = parser.get_structure("name", args['pdb'])
fill = s[int(args['model'])][args['chain']]
# retrieve the pdb id of the input file
pdb_id = str(args['pdb']).split(".")[0]
# retrieve chain amino acids
ppb = PPBuilder()
for pp in ppb.build_peptides(fill):
    aa_chain = str(pp.get_sequence())
# choose program
if args['program'] == 1:
    # fix the index for start parameter
    if args['start'] > 0:
        aa_start = args['start'] -1
    else:
        print("-start parameter must be a positive integer")
        exit(1)
    # fix the index for end parameter
    if args['end'] > 0:
        aa_end = args['end'] -1
    else:
        aa_end = args['end']
else:
    
    # fix the index for start parameter
    if args['start'] > 0:
        aa_start = args['start'] -1
    else:
        print("-start parameter must be a positive integer")
        exit(1)
    # fix the index for end parameter
    args['end'] = len(aa_chain) -1
    aa_end = args['end']
# subset based on aa in chain
sub_seq = aa_chain[aa_start:aa_end]
# export to fasta
record = SeqRecord(Seq(sub_seq),id="".join([str(pdb_id),"_",str(args['chain']),"_",str(args['start']),"_",str(args['end'])]),description="")
SeqIO.write(record, "".join([str(pdb_id),"_",str(args['chain']),"_",str(args['start']),"_",str(args['end']),".fasta"]), "fasta")
