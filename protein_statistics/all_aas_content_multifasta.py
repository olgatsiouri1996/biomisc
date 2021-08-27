# python3
import argparse
from Bio import SeqIO
import pandas as pd
# input parameters
ap = argparse.ArgumentParser(description="calculates the amino acid content of each amino acid for each input sequence")
ap.add_argument("-in", "--input_file", required=True, help="input fasta file")
ap.add_argument("-out", "--output_file", required=True, help="output txt file")
args = vars(ap.parse_args())
# create aa_content function
def aa_content(seq,aa):
  return round((seq.count(str(aa)) / len(seq)) * 100, 2)
# main
# retrieve headers
headers = []  # setup empty list
for record in SeqIO.parse(args['input_file'], "fasta"):
    headers.append(record.id)
df = pd.DataFrame()
df['protein_id'] = headers
# create list with 1-letter IUPAC aminoacid codes
aa_list = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y","B","J","Z","X"]
# retrieve content for each amino acid
content = [] # setup empty list
for i in aa_list:
    for record in SeqIO.parse(args['input_file'], "fasta"):
        # add this record to the list
        content.append(aa_content(record.seq,i))
    df[str(i)] = content
    content.clear()
# export
with open(args['output_file'], 'a') as f:
    f.write(
        df.to_csv(header = True, index = False, sep= "\t", line_terminator= '\n')
    )

