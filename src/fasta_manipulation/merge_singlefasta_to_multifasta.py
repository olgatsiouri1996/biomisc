# python3
import argparse
import os
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-dir", "--directory", required=True,  help="input directory with fasta files")
ap.add_argument("-fa", "--multifasta", required=True,  help="output multi-fasta file")
args = vars(ap.parse_args())
# main
DIR = args['directory']
oh = open( args['multifasta'], 'w')
for f in os.listdir(DIR):
    fh = open(os.path.join(DIR, f))
    for line in fh:
        oh.write(line)
    fh.close()
oh.close()


