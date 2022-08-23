# python3
import sys
import argparse
import pyfastx
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in","--input", required=False, help="input multi-fasta file(all fasta records should either have no fasta description or all of them should have fasta description)")
ap.add_argument("-pro", "--program", required=False, default=1, type=int, help="output to choose: 1) 2-column txt file with fasta identifiers and fasta sequences 2) 2-column txt file with full fasta headers and fasta sequences 3) 3-column txt file with fasta identifiers, fasta descriptions and fasta sequences. Default is 1")
ap.add_argument("-out","--output", required=True, help="output txt file")
args = vars(ap.parse_args())
# main
# choose program
if args['program'] == 1:
    sys.stdout = open(args['output'], 'w')
    for name,seq,comment in pyfastx.Fastx(args['input']):
        print(name,seq,sep='\t')  
    sys.stdout.close()
elif args['program'] == 2:
    sys.stdout = open(args['output'], 'w')
    for name,seq,comment in pyfastx.Fastx(args['input']):
        print(' '.join([name,comment]),seq,sep='\t')
    sys.stdout.close()
else:
    sys.stdout = open(args['output'], 'w')
    for name,seq,comment in pyfastx.Fastx(args['input']):
        print(name,comment,seq,sep='\t')  
    sys.stdout.close()
