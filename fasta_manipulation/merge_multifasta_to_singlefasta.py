# python3
import argparse
from Bio import SeqIO
import sys
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-mfa", "--multifasta", required=True,  help="input multi-fasta file to merge its sequences")
ap.add_argument("-id", "--seqid", required=True, help="fasta header of the output file")
ap.add_argument("-sfa", "--singlefasta", required=True,  help="output single-fasta file")
args = vars(ap.parse_args())
# main
sequences = []  # setup an empty list
for record in SeqIO.parse(args['multifasta'], "fasta"):
	sequences.append(record.seq)
# output
sys.stdout = open(args['singlefasta'], 'a')
print(">"+args['seqid'], ''.join(map(str,sequences)), sep='\n')
sys.stdout.close()



  
  
