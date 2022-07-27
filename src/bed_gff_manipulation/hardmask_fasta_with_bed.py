# python3
import argparse
from pyfaidx import Fasta
import pandas as pd
import warnings
# input parameters
ap = argparse.ArgumentParser(description="ovewrite and hardmask a multi-fasta file with N nucleotides")
ap.add_argument("-bed", "--bed", required=True, help="input bed file(made with bedops)")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
args = vars(ap.parse_args())
# main
# ignore warnings
warnings.filterwarnings('ignore')
# import bed with no headers specified
df = pd.read_csv(args['bed'], sep= "\t", header=None)
# convert each column to list
chrom = df.iloc[:,0].values.tolist()
start = df.iloc[:,1].values.tolist()
end = df.iloc[:,2].values.tolist()
# import fasta file
features = Fasta(args['input'],mutable=True)
# iterate all below lists in pairs
for (a, b, c) in zip(chrom, start, end):
    features[str(a)][int(b):int(c)] = 'N'*len(features[str(a)][int(b):int(c)].seq)
        