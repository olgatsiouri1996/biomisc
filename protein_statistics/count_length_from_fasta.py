# python3
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-out", "--output_file", required=True, help="output txt file")
args = vars(ap.parse_args())
# main
headers = []
lengths = [] # setup  empty lists
for record in SeqIO.parse(args['input_file'], "fasta"):
        # add this record to the lists
   lengths.append(len(record.seq))
   headers.append(record.id)
# create data frame
df = pd.DataFrame()
df['id'] = headers
df['length'] = lengths
# export
with open(args['output_file'], 'a') as f:
    f.write(
        df.to_csv(header = True, index = False, sep= "\t", doublequote= False, line_terminator= '\n')
    )

