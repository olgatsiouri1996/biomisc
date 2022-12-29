# python3
import os
import sys
import argparse
from biopandas.pdb import PandasPdb
# input parameters
ap = argparse.ArgumentParser(description="converts a pdb file into a single or multi-fasta file based on the chain, start and end locations")
ap.add_argument("-in", "--input", required=False, help="input pdb file")
ap.add_argument("-fasta", "--fasta", required=False, help="output multi-fasta file")
ap.add_argument("-dir", "--directory", required=False, type=str, default='', help="directory to search for pdb files(the directory can contain many filetypes). Default is the current directory")
ap.add_argument("-out", "--output", required=False, type=str, default='', help="directory to save 1 or more single-fasta files(the directory can contain many filetypes). Default is the current directory")
ap.add_argument("-chain", "--chain", required=False, default='A', help="chain from pdb file to select. Default is A")
ap.add_argument("-start", "--start", required=False, default=1, type=int, help="amino acid in chain to start writing the fasta file. Default is 1")
ap.add_argument("-end", "--end", required=False, type=int, help="amino acid in chain to end writing the fasta file")
ap.add_argument("-type", "--type", required=False,default=1, type=int, help="type of input to choose: 1) 1 pdb file, 2) many pdb files. Default is 1")
ap.add_argument("-pro", "--program", required=False,default=1, type=int, help="program to choose: 1) add both start and end location 2) the end location will be that of the latest amino acid in the chain. Default is 1")
ap.add_argument("-mfa", "--multifasta", required=False,default='no', type=str, help="output as multi-fasta?. Default is no")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create function to trim + convert to fasta
def trim_to_fasta(fi):
    # insert pdb file
    ppdb = PandasPdb()
    ppdb.read_pdb(fi)
    # convert 3 letters aa to 1
    one = ppdb.amino3to1()
    # select chain and convert to string
    sequence = ''.join(one.loc[one['chain_id']==args['chain'],'residue_name'])
    # choose end location
    if args['program'] == 1:
        seq_end = args['end']
    else:
        seq_end = len(sequence)
    # subset by location
    prot = sequence[int(args['start'] -1):seq_end]
    # remove dataframes and lists
    del ppdb; del one
    if args['type'] ==1:
        # get pdb file basename
        basename = str(os.path.basename(fi)).split('.')[0]
    else:
        basename = str(fi).split('.')[0]
    # export to fasta
    if args['multifasta']=='no':
        sys.stdout = open(os.path.join(args['output'],''.join([basename,"_",args['chain'],"_",str(args['start']),"_",str(seq_end),".fasta"])), 'a')
        print(''.join([">",basename,"_",args['chain'],"_",str(args['start']),"_",str(seq_end)]).replace('\r',''))
        print('\n'.join(split_every_60(prot)))
        sys.stdout.close()
    else:
        print(''.join([">",basename,"_",args['chain'],"_",str(args['start']),"_",str(seq_end)]).replace('\r',''))
        print('\n'.join(split_every_60(prot)))            
# select between importing 1 or many pdb files
if args['type'] == 1:
    trim_to_fasta(args['input'])
else:
     # import each pdb file from the working directory
    if args['multifasta']=='no':
        for filename in sorted(os.listdir(os.chdir(args['directory']))):
            if filename.endswith(".pdb"):
               trim_to_fasta(filename)
    else:
        sys.stdout = open(args['fasta'],'a')
        for filename in sorted(os.listdir(os.chdir(args['directory']))):
            if filename.endswith(".pdb"):
               trim_to_fasta(filename)
        sys.stdout.close()

