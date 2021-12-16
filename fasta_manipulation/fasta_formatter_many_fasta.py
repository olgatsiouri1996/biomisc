# python3
import os
import argparse
from Bio import SeqIO
import sys
# input parameters
ap = argparse.ArgumentParser(description="changes the width of sequences line in multiple FASTA file by specifying either the width")
ap.add_argument("-w", "--width", required=False, type=int, default=80, help="number of characters per line. Default 80")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters
def split_every_width(s,w): return [s[i:i+w] for i in range(0,len(s),w)]
# setup empty list 
names = []
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        # export to new fasta files with the user imported width value
        sys.stdout = open(''.join([filename.split(".")[0],"_","w",str(args['width']),".fasta"]), 'a')
        for record in SeqIO.parse(filename,'fasta'):
                print(">"+record.id)
                print('\n'.join(split_every_width(str(record.seq), args['width']))) # add characters in new line after the number of characters surpasses the input width 
        sys.stdout.close()

