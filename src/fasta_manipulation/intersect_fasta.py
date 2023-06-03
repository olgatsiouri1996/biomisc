# python3
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa1", "--fasta1", required=True, help="input multi fasta file")
ap.add_argument("-fa2", "--fasta2", required=True, help="input multi fasta file")
ap.add_argument("-pro", "--program", type=int, default=1, required=False, help="program to choose: 1. export the sequences of fasta1 that have the same identifiers as fasta2, 2. export the sequences of fasta1 that don't have the same identifiers as fasta2. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output multi fasta file")
args = vars(ap.parse_args())
# main
# helper function to wrap fasta sequence to 60 characters per line
def wrap_fasta_seq(seq):
    return '\n'.join([seq[i:i+60] for i in range(0, len(seq), 60)])
# create fasta index
features1 = Fasta(args['fasta1'])
features2 = Fasta(args['fasta2'])
## choose program
if args['program'] == 1:
    # find common ids of the 2 files
    final = (set(features1.keys()).intersection(features2.keys()))
else:
    final = (set(features1.keys()).difference(features2.keys()))
# export to fasta
with open(args['output'], 'w') as f:
    for fin in final:
        f.write(f'>{str(features1[str(fin)].long_name).rstrip()}\n{wrap_fasta_seq(features1[str(fin)][:].seq)}\n')

