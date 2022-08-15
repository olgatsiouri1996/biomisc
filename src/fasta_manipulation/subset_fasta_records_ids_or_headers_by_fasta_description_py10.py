# python3
import sys
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-ma", "--match", required=True, type=str, help="word or phrase to search in each fasta header(no regular expression, differentiates between capital or non capital letters)")
ap.add_argument("-out", "--output", required=False, help="output multi-fasta file. File can be appended")
ap.add_argument("-headers", "--headers", required=False, help="1 or 2-column tab seperated txt file to save the output fasta identifiers or full fasta headers respectively. File can be appended")
ap.add_argument("-pro", "--program", required=False, type=int, default=1, help="Program to choose: 1) collect fasta records with headers that match the pattern 2) collect only fasta identifiers, 3) collect full fasta headers. Default is 1")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# choose program
program = args['program']
match program:
    case 1:
        # iterate input headers to extract sequences and export as multi-fasta
        sys.stdout = open(args['output'], 'a')
        for header in features.keys():
            if args['match'] in features[str(header)].long_name:
                print(''.join([">",features[str(header)].long_name]).replace('\r', ''))
                print('\n'.join(split_every_60(features[str(header)][:].seq)))
        sys.stdout.close()
    case 2:
        # export to 1-column txt file
        with open(args['headers'], 'a') as filehandle:
            for key in features.keys():
                if args['match'] in features[key].long_name:
                    filehandle.write('%s\n' % key)
    case 3:
        # export to 1-column txt file
        with open(args['headers'], 'a') as filehandle:
            for key in features.keys():
                if args['match'] in features[key].long_name:
                    filehandle.write('%s\n' % '\t'.join([key,str(features[key].long_name).split(key)[1]]))
