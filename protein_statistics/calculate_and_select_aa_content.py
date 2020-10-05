# python3
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-max", "--max_aa", required=True, help="max threshold of aa content, type = float")
ap.add_argument("-min", "--min_aa", required=True, help="min threshold of aa content, type = float")
ap.add_argument("-aa", "--aa_type", required=True, help="aa to search the content for")
ap.add_argument("-out", "--output_file", required=True, help="output txt file")
args = vars(ap.parse_args())
# create aa_content function
def aa_content(seq):
  return round((seq.count(args['aa_type']) / len(seq)) * 100, 2)
# main
content = []
headers = []  # setup empty lists
for record in SeqIO.parse(args['input_file'], "fasta"):
    if float(args['min_aa']) < aa_content(record.seq) < float(args['max_aa']):
        # add this record to the list
        headers.append(record.id)
        content.append(aa_content(record.seq))
# create data frame
df = pd.DataFrame()
df['protein_id'] = headers
df[args['aa_type']] = content
# export
with open(args['output_file'], 'a') as f:
    f.write(
        df.to_csv(header = True, index = False, sep= "\t", line_terminator= '\n')
    )

