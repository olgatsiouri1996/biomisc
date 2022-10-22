# python3
import argparse
import os
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=False, help="input file to change the extension")
ap.add_argument("-ext", "--extension", required=False, type=str, default='.fasta', help="extension to change into")
ap.add_argument("-num", "--number", required=False, type=str, default='one', help="number of  files to change extensions: one, many. Default is one")
args = vars(ap.parse_args())
# main
# function to change the file extension
def change_extension(fi):
    base = os.path.splitext(fi)[0]
    os.rename(fi, base + args['extension'])
# choose number of input files
if args['number'] == 'one':
    change_extension(args['input'])
else:
    for filename in sorted(os.listdir(os.getcwd())):
        change_extension(filename)
