# python3
import argparse
import os
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=False, type=str, default='.fsta', help="input file extension. Default is .fsta")
ap.add_argument("-ext", "--extension", required=False, type=str, default='.fasta', help="extension to change into. Default is .fasta")
ap.add_argument("-num", "--number", required=False, type=str, default='one', help="number of input file extensions: one, many. if set to many it can only be used to folders that contain only the files that you want to change the extension. Default is one")
args = vars(ap.parse_args())
# main
# change the file extension
if args['number']=='one':
    for filename in sorted(os.listdir(os.getcwd())):
        if filename.endswith(args['input']):
            base = os.path.splitext(filename)[0]
            os.rename(filename, base + args['extension'])
else:
    for filename in sorted(os.listdir(os.getcwd())):
        base = os.path.splitext(filename)[0]
        os.rename(filename, base + args['extension'])