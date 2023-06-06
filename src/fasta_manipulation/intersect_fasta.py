# python3
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa1", "--fasta1", required=True, help="input multi fasta file")
ap.add_argument("-fa2", "--fasta2", required=True, help="input multi fasta file")
ap.add_argument("-pro", "--program", type=int, default=1, required=False, help="program to choose: 1. export the sequences of fasta1 that have the same identifiers as fasta2, 2. export the sequences of fasta1 that don't have the same identifiers as fasta2. Default is 1")
ap.add_argument("-type", "--type", type=int, default=1, required=False, help="output type to export to. 1. 1 multi-fasta file, 2. 2-column tab seperated txt file with id and seq as columns, 3. 2-column tab seperated txt file with id and description as columns, 4. 3-column tab seperated txt file with id, description and seq as columns. Default is 1")
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
# choose export type
type = args['type']
match type:
    case 1:
        # export to fasta
        with open(args['output'], 'w') as f:
            for fin in final:
                f.write(f'>{str(features1[str(fin)].long_name).rstrip()}\n{wrap_fasta_seq(features1[str(fin)][:].seq)}\n')
    case 2:
        with  open(args['output'], 'w') as f:
                f.write(f'{"id"}\t{"seq"}\n')
                for fin in final:
                    f.write(f'{str(fin)}\t{features1[str(fin)][:].seq}\n')
    case 3:
        with  open(args['output'], 'w') as f:
                f.write(f'{"id"}\t{"description"}\n')
                for fin in final:
                    try:
                        f.write(f'{str(fin)}\t{str(str(features1[str(fin)].long_name).rstrip()).split(" ",1)[1]}\n')
                    except IndexError:
                        f.write(f'{str(fin)}\t{""}\n')
    case 4:
        with  open(args['output'], 'w') as f:
                f.write(f'{"id"}\t{"description"}\t{"seq"}\n')
                for fin in final:
                    try:
                        f.write(f'{str(fin)}\t{str(str(features1[str(fin)].long_name).rstrip()).split(" ",1)[1]}\t{features1[str(fin)][:].seq}\n')
                    except IndexError:
                        f.write(f'{str(fin)}\t{""}\t{features1[str(fin)][:].seq}\n')
