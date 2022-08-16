# python3
import argparse
from pyfaidx import Fasta
import sys
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-mfa", "--multifasta", required=True,  help="input multi-fasta file to merge its sequences")
ap.add_argument("-id", "--seqid", required=True, type=str, help="fasta header of the output file")
ap.add_argument("-sp", "--spacer", required=False, type=str, default="", help="nucleotides or aminoacids to add between the merged fasta sequences. Default: no sequence to add")
ap.add_argument("-sfa", "--singlefasta", required=True,  help="output single-fasta file")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# index fasta file
features = Fasta(args['multifasta'],as_raw=True)
# store all sequences to a list
sequences = [features[key][:] for key in features.keys()]
# merge all sequences at 1 and create SeqRecord object
merged_seqs = args['spacer'].join(sequences)
# export to fasta
sys.stdout = open(args['singlefasta'], 'a')
print(''.join([">",args['seqid']]).replace('\r',''))
print('\n'.join(split_every_60(merged_seqs)))
sys.stdout.close()
