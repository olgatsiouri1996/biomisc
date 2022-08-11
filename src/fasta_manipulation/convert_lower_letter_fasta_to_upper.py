# python3
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser(description="ovewrite and convert a fasta with lowercase letters to uppercase")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
args = vars(ap.parse_args())
# main
# import fasta file
features = Fasta(args['input'],mutable=True)
# iterate all below lists in pairs
for key in features.keys():
    features[key][:] = str(features[key][:].seq).upper()

