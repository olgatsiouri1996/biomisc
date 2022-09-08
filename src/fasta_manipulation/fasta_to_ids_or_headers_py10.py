# python3
import argparse
from pyfaidx import Fasta
# input arguments
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-txt", "--txt", required=True, help="1 or 2-column txt file to save the output fasta identifiers or full fasta  headers with identifier and description respectively")
ap.add_argument("-desc", "--description", required=False, type=str, default='F', help="Collect fasta description along with fasta identifiers? Default is F")
args = vars(ap.parse_args())
# main
# index multi-fasta file
features = Fasta(args['input'])
# choose program
program = args['description']
match program:
    case 'F':
        # export to a 1-column txt file
        with open(args['txt'], 'w') as filehandle:
            for key in features.keys():
                filehandle.write('%s\n' % key)
    case 'T':
        # export to a 2-column txt file
        with open(args['txt'], 'w') as filehandle:
            for key in features.keys():
                try:
                    description = str(features[key].long_name).split(' ',1)[1]
                except IndexError:
                    description = ""

                filehandle.write('%s\n' % '\t'.join([key,description]))

