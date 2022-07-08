# python3
import sys
import argparse
from pyfaidx import Fasta
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program",type=int, default=1, required=False, help="choose to output a fasta file or a txt file with headers(1.fasta file with sequence length in fasta description, 2.txt file with headers. Defaults to 1)")
ap.add_argument("-out", "--output", required=False, help="output fasta file")
ap.add_argument("-max", "--max", required=False, default=300, help="max number of sequence length. Default is 300")
ap.add_argument("-min", "--min", required=False, default=1, help="min number of sequence length. Default is 1")
ap.add_argument("-headers", "--headers", required=False, help="file to save the output fasta headers")
args = vars(ap.parse_args())
# main
# choose program
program = args['program']
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create fasta index
features = Fasta(args['input'])
# select sequences
if program == 1:
    sys.stdout = open(args['output'], 'a')
    for key in features.keys():
        if int(args['min']) <= features[key][:].end <= int(args['max']):
            print(''.join([">",features[key].long_name," ","length:"," ",str(features[key][:].end)]))
            print('\n'.join(split_every_60(features[key][:].seq)))
    sys.stdout.close()
# retrieve headers only
else:
    # export to txt
    with open(args['headers'], 'w') as filehandle:
        for key in features.keys():
            if int(args['min']) <= features[key][:].end <= int(args['max']):
                filehandle.write('%s\n' % key)

