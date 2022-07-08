# python3
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program", type=int, default=1, required=False, help="program to choose: 1. output the length of all sequences, 2. output the length of the sequences that fall under a specific min,max threshold. Defaults to 1)")
ap.add_argument("-max", "--max", required=False, default=300, help="max number of sequence length. Default is 300")
ap.add_argument("-min", "--min", required=False, default=1, help="min number of sequence length. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output txt file, with columns the id, length and fasta descriptions")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# create fasta index
features = Fasta(args['input'])
# choose program
program = args['program']
# export for all sequences
if program == 1:
   # export to txt
    with open(args['output'], 'w') as filehandle:
        for key in features.keys():
            filehandle.write('%s\n' % '\t'.join([key,str(features[key][:].end),str(features[key].long_name).split(key)[1]]))
# subset based on max, min values
else:
    # export to txt
    with open(args['output'], 'w') as filehandle:
        for key in features.keys():
            if int(args['min']) <= features[key][:].end <= int(args['max']):
                filehandle.write('%s\n' % '\t'.join([key,str(features[key][:].end),str(features[key].long_name).split(key)[1]]))