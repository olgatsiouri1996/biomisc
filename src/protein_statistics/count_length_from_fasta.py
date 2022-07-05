# python3
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program", type=int, default=1, required=False, help="program to choose: 1. output the length of all sequences, 2. output the length of the sequences that fall under a specific min,max threshold. Defaults to 1)")
ap.add_argument("-max", "--max", required=False, default=300, help="max number of sequence length. Default is 300")
ap.add_argument("-min", "--min", required=False, default=1, help="min number of sequence length. Default is 1")
ap.add_argument("-out", "--output", required=True, help="output txt file, with columns the id, length and fasta descriptions")
args = vars(ap.parse_args())
# main
headers = []
lengths = []
descriptions = [] # setup  empty lists
# choose program
program = args['program']
# export for all sequences
if program == 1:
    for record in SeqIO.parse(args['input'], "fasta"):
        # add this record to the lists
        lengths.append(len(record.seq))
        headers.append(record.id)
        descriptions.append(str(record.description).split(record.id)[1])
    # create data frame
    df = pd.DataFrame()
    df['id'] = headers
    df['length'] = lengths
    df['description'] = descriptions
    #print(df)
    # export
    with open(args['output'], 'a') as f:
        f.write(
            df.to_csv(header = True, index = False, sep= "\t", doublequote= False, escapechar='\\', line_terminator= '\n')
        )
# subset based on max, min values
else:
    for record in SeqIO.parse(args['input'], "fasta"):
        if float(args['min']) <= len(record.seq) <= float(args['max']):
            # add this record to the list
            headers.append(record.id)
            lengths.append(len(record.seq))
            descriptions.append(str(record.description).split(record.id)[1])
    # create data frame
    df = pd.DataFrame()
    df['id'] = headers
    df['length'] = lengths
    df['description'] = descriptions
    # export
    with open(args['output'], 'a') as f:
        f.write(
            df.to_csv(header = True, index = False, sep= "\t", escapechar='\\', line_terminator= '\n')
        )


