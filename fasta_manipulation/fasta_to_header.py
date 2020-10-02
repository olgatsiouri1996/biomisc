# python3
import argparse
from Bio import SeqIO
# input arguments
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-headers", "--fasta_headers", required=True, help="file to save the output fasta headers")
args = vars(ap.parse_args())
# main
headers = []
for record in SeqIO.parse(args['input_file'], "fasta"):
    headers.append(record.id)
with open(args['fasta_headers'], 'w') as filehandle:
    for listitem in headers:
        filehandle.write('%s\n' % listitem)
