# python3
import os
import argparse
from Bio.PDB import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-pdb", "--pdb", required=False, help="input pdb file")
ap.add_argument("-model", "--model",default=0, required=False, help="model from pdb file to select(integer). Default is 0(1 model only)")
ap.add_argument("-chain", "--chain", required=False, default='A', help="chain from pdb file to select")
ap.add_argument("-start", "--start", required=False,default=1, type=int, help="amino acid in chain to start writing the fasta file. Default is 1")
ap.add_argument("-end", "--end", required=False, type=int, help="amino acid in chain to end writing the fasta file")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose 1) add both start and end location 2) the end location will be that of the latest amino acid in the chain. Default is 1")
ap.add_argument("-type", "--type", required=False,default=1, type=int, help="type of input to choose. 1) 1 pdb file, 2) many pdb files. Default is 1")
args = vars(ap.parse_args())
# main
# create function to trim + convert to fasta
def trim_to_fasta(fi):
    # select chain
    fill = s[int(args['model'])][args['chain']]
    # select between importing 1 or many pdb files
    if args['type'] == 1:
        # retrieve the pdb id of the input file
        pdb_id = str(fi).split(".")[0]
    else:
        pdb_id = fi.split(".")[0]
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
        # add end parameter
        aa_end = args['end']
    else:
        # fix the index for start parameter
        if args['start'] > 0:
            aa_start = args['start'] -1
        else:
            print("-start parameter must be a positive integer")
            exit(1)
        # add end parameter according to program 2
        args['end'] = len(aa_chain)
        aa_end = args['end']
    # subset based on aa in chain
    sub_seq = aa_chain[aa_start:aa_end]
    # export to fasta
    record = SeqRecord(Seq(sub_seq),id="".join([str(pdb_id),"_",str(args['chain']),"_",str(args['start']),"_",str(args['end'])]),description="")
    return SeqIO.write(record, "".join([str(pdb_id),"_",str(args['chain']),"_",str(args['start']),"_",str(args['end']),".fasta"]), "fasta")
# select between importing 1 or many pdb files
if args['type'] == 1:    
    parser = PDBParser()
    s = parser.get_structure("name", args['pdb'])
    trim_to_fasta(args['pdb'])
else:
    # import each fasta file from the working directory
    for filename in sorted(os.listdir(str(os.getcwd()))):
        if filename.endswith(".pdb"):
            parser = PDBParser()
            s = parser.get_structure("name", filename)
            trim_to_fasta(filename)
