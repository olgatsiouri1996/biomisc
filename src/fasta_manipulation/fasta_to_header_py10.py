# python3
import argparse
from pyfaidx import Fasta
# input arguments
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-headers", "--headers", required=True, help="1-column txt file to save the output fasta headers")
ap.add_argument("-pro", "--program", required=False, type=int, default=1, help="Program to choose. 1) collect only fasta identifiers, 2) collect fasta headers. Default is 1")
args = vars(ap.parse_args())
# main
# index multi-fasta file
features = Fasta(args['input'])
# choose program
program = args['program']
match program:
    case 1:
        # export to 1-column txt file
        with open(args['headers'], 'w') as filehandle:
            for key in features.keys():
                filehandle.write('%s\n' % key)
    case 2:
        # export to 1-column txt file
        with open(args['headers'], 'w') as filehandle:
            for key in features.keys():
                filehandle.write('%s\n' % '\t'.join([key,str(features[key].long_name).split(key)[1]]))