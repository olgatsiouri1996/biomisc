# python3
import os
import sys
import argparse
from biopandas.pdb import PandasPdb
# input parameters
ap = argparse.ArgumentParser(description="converts each pdb files into single fasta files or makes a multi-fasta file based on the chain, start and end locations")
ap.add_argument("-in", "--input", required=True, help="input 4-column txt file with pdb filename(no extension),chain,start and end coordinates")
ap.add_argument("-mfa", "--multifasta", required=False, help="output multi-fasta file")
ap.add_argument("-dir", "--directory", required=False, type=str, default='.', help="directory to search for pdb files(the directory can contain many filetypes).Default is the current directory")
ap.add_argument("-type", "--type", required=False,default=1, type=int, help="type of output to choose: 1) 1 multi-fasta file, 2) many single-fasta files. Default is 1")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# convert a 4-column txt file to 4 generators 1 per column
pdbname = (str(line.rstrip()).split()[0] for line in open(args['input']))
chain = (str(line.rstrip()).split()[1] for line in open(args['input']))
start = (int(str(line.rstrip()).split()[2]) for line in open(args['input']))
end = (int(str(line.rstrip()).split()[3]) for line in open(args['input']))
# create function to trim + convert to fasta
def trim_to_fasta(fi,ch,st,en):
    # insert pdb file
    ppdb = PandasPdb()
    ppdb.read_pdb(''.join([fi,'.pdb']))
    # convert 3 letters aa to 1
    one = ppdb.amino3to1()
    # select chain and convert to string
    sequence = ''.join(one.loc[one['chain_id']==ch,'residue_name'])
    # subset by location
    prot = sequence[int(st -1):en]
    # remove dataframes and lists
    del ppdb; del one
    return prot
# select input dir
os.chdir(args['directory'])
# select between exporting 1 or many fasta files
if args['type'] == 1:
    sys.stdout = open(args['multifasta'],'a')
    for (a,b,c,d) in zip(pdbname,chain,start,end):
        print(''.join([">",a,"_",b,"_",str(c),"_",str(d)]).replace('\r',''))
        print('\n'.join(split_every_60(trim_to_fasta(a,b,c,d))))
    sys.stdout.close()
else:
    for (a,b,c,d) in zip(pdbname,chain,start,end):
        sys.stdout = open(''.join([a,"_",b,"_",str(c),"_",str(d),".fasta"]), 'a')
        print(''.join([">",a,"_",b,"_",str(c),"_",str(d)]).replace('\r',''))
        print('\n'.join(split_every_60(trim_to_fasta(a,b,c,d))))
        sys.stdout.close()            
