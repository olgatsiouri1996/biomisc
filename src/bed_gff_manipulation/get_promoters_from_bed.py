# python3
import argparse
import pandas as pd
from pyfaidx import Fasta
import textwrap

# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-bed", "--bed", required=True, help="input bed file with 5 columns: gene id, chromosome/scaffold/contig, start, end strand")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
ap.add_argument("-pro", "--promoter", required=False, default=2000, type=int, help="promoter length. Default is 2000")
args = vars(ap.parse_args())
# Read BED file into a pandas DataFrame
bed_df = pd.read_csv(args['bed'], sep='\t', header=None, names=['a', 'b', 'c', 'd', 'e'])

# Import FASTA file
features = Fasta(args['input'])

def process_positive_strand(row):
    a, b, c, _, _ = row
    promoter_length = int(args['promoter'])

    start_pos = max(1, int(c) - promoter_length - 1)
    end_pos = int(c)
    header = f">{a} {b}:{start_pos}-{end_pos}"
    sequence = features[str(b)][start_pos - 1:end_pos].seq
    wrapped_sequence = textwrap.fill(sequence, width=60)

    return f"{header}\n{wrapped_sequence}"

def process_negative_strand(row):
    a, b, _, d, _ = row
    promoter_length = int(args['promoter'])

    start_pos = int(d)
    end_pos = min(int(d) + promoter_length, features[str(b)][:].end)
    header = f">{a} {b}:{start_pos}-{end_pos} reverse complement"
    sequence = features[str(b)][start_pos - 1:end_pos].reverse.complement.seq
    wrapped_sequence = textwrap.fill(sequence, width=60)
    
    return f"{header}\n{wrapped_sequence}"

# Split dataframe by strand and process each strand separately
positive_strand_df = bed_df[bed_df['e'] == '+']
negative_strand_df = bed_df[bed_df['e'] == '-']

# Process genes for each strand
positive_strand_promoters = positive_strand_df.apply(process_positive_strand, axis=1)
negative_strand_promoters = negative_strand_df.apply(process_negative_strand, axis=1)

# Combine the results
all_promoters = positive_strand_promoters.tolist() + negative_strand_promoters.tolist()

# Export to fasta
with open(args['output'], 'w') as output_file:
    output_file.write('\n'.join(all_promoters))
