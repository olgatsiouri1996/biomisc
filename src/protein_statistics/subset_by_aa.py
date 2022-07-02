# python3
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-pro", "--program",type=int, default=1, required=False, help=" program to choose the output format 1) fasta with aa percentage in fasta description, 2) txt file with headers 3) tab file with fasta headers,aa content percentage and fasta description as columns. Defaults to 1)")
ap.add_argument("-max", "--max", required=False, default=100, help="max threshold of aa content, type = float. Default is 100")
ap.add_argument("-min", "--min", required=False, default=0, help="min threshold of aa content, type = float.  Default is 0")
ap.add_argument("-aa", "--aa", required=True, help="aa to search the content for")
ap.add_argument("-headers", "--headers", required=False, help="file to save the output fasta headers")
ap.add_argument("-fasta", "--fasta", required=False, help="output fasta file")
ap.add_argument("-txt", "--txt", required=False, help="output txt file with fasta headers, aa content percentage and fasta description as columns")
args = vars(ap.parse_args())
# create aa_content function
def aa_content(seq):
    return round((seq.count(args['aa']) / len(seq)) * 100, 2)
# main
# choose program
program = args['program']
# select sequences
if program == 1:
    sequences = []  # setup an empty list
    for record in SeqIO.parse(args['input'], "fasta"):
        if float(args['min']) <= aa_content(record.seq) <= float(args['max']):
            record.description = ''.join(["%",args['aa']," ","content:"," ",str(aa_content(record.seq))," ",str(record.description).split(record.id)[1]])
            # add this record to the list
            sequences.append(record)
    # export to fasta
    SeqIO.write(sequences, args['fasta'], "fasta")
# retrieve headers only
elif program == 2:
    headers = []  # setup an empty list
    for record in SeqIO.parse(args['input'], "fasta"):
        if float(args['min']) <= aa_content(record.seq) <= float(args['max']):
            # add this record to the list
            headers.append(record.id)
    # export to txt
    with open(args['headers'], 'w') as filehandle:
        for listitem in headers:
            filehandle.write('%s\n' % listitem)
else:
    content = []
    headers = []
    description = []  # setup empty lists
    for record in SeqIO.parse(args['input'], "fasta"):
        if float(args['min']) <= aa_content(record.seq) <= float(args['max']):
            # add this record to the list
            headers.append(record.id)
            content.append(aa_content(record.seq))
            description.append(str(record.description).split(record.id)[1])
    # create data frame
    df = pd.DataFrame()
    df['protein_id'] = headers
    df[''.join(["%",args['aa']])] = content
    df['description'] = description
    # export
    with open(args['txt'], 'a') as f:
        f.write(
            df.to_csv(header = True, index = False, sep= "\t", line_terminator= '\n')
        )

