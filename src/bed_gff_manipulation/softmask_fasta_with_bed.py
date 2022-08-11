# python3
import argparse
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser(description="ovewrite and softmask a multi-fasta file")
ap.add_argument("-bed", "--bed", required=True, help="input bed file(made with bedops)")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
args = vars(ap.parse_args())
# main
# setup empty lists
chrom = []
start = []
end = []
# import bed 
with open(args['bed'], 'r') as f:
    for line in f:
        # convert each column to list
        chrom.append(line.split()[0])
        start.append(line.split()[1])
        end.append(line.split()[2])
# import fasta file
features = Fasta(args['input'],mutable=True)
# iterate all below lists in pairs
for (a, b, c) in zip(chrom, start, end):
    features[str(a)][int(b):int(c)] = str(features[str(a)][int(b):int(c)].seq).lower()

