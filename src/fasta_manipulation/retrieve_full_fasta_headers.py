# python3
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser(description="retrieve fasta identifiers and their descriptions")
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-headers", "--headers", required=True, help="1-column txt file to save the output fasta headers with descriptions")
args = vars(ap.parse_args())
# main
# import fasta file
features = Fasta(args['input'])
# export to 1-column txt file
with open(args['headers'], 'w') as filehandle:
    for key in features.keys():
        filehandle.write('%s\n' % features[str(key)].long_name)

