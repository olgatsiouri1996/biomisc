# python3
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input multi-fasta file")
ap.add_argument("-bed", "--bed", required=True, help="output bed file with id start and end locations")
args = vars(ap.parse_args())
# main
# import fasta file
features = Fasta(args['input'])
# export to 1-column txt file
with open(args['bed'], 'w') as filehandle:
    for key in features.keys():
        filehandle.write('%s\n' % '\t'.join([key,"1",str(features[key][:].end)]))

