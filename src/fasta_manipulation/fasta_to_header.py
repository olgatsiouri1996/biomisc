# python3
import argparse
from pyfaidx import Fasta
# input arguments
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-headers", "--headers", required=True, help="1-column txt file to save the output fasta headers")
args = vars(ap.parse_args())
# main
# index multi-fasta file
features = Fasta(args['input'])
# export to 1-column txt file
with open(args['headers'], 'w') as filehandle:
    for key in features.keys():
        filehandle.write('%s\n' % key)
