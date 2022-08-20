# python3
import argparse
import sys
import pyfastx
# input arguments
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-txt", "--txt", required=True,  help="1 or 2-column txt file to save the output fasta identifiers or full fasta  headers with identifier and description respectively")
ap.add_argument("-pro", "--program", required=False, type=int, default=1, help="program to choose: 1. retrieve only fasta identifiers 2. retrieve fasta identifiers and fasta headers (tab seperated). Default is 1")
args = vars(ap.parse_args())
# main
# retrieve only the fasta identifier
if args['program'] == 1:
    sys.stdout = open(args['txt'], 'w')
    for name,seq,comment in pyfastx.Fastx(args['input']):
        print(name)
    sys.stdout.close()
# retrieve full fasta headers
else:
    sys.stdout = open(args['txt'], 'w')
    for name,seq,comment in pyfastx.Fastx(args['input']):
        print(name, comment,sep='\t')
    sys.stdout.close()
