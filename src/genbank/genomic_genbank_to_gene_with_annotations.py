# python3
import argparse
from Bio import SeqIO, SeqFeature
import os
# imput parameters
ap = argparse.ArgumentParser(description="retrieve gene from genbank with annotations")
ap.add_argument("-in", "--input", required=True, help="input genomic genbank file")
ap.add_argument("-chr", "--chr", required=True, type=str, help="chromosome/scaffold/contig the gene is located")
ap.add_argument("-start", "--start", required=True, type=int, help="start of the gene in the chromosome/scaffold/contig")
ap.add_argument("-end", "--end", required=True, type=int, help="end of the gene in the chromosome/scaffold/contig")
ap.add_argument("-dir", "--directory", required=False, type=str, default='.', help="directory to save the output genbank file. Default is the current directory")
args = vars(ap.parse_args())
# retrieve the gene with annotations from the genomic genbank file
for record in SeqIO.parse(args['input'], "genbank"):
	if record.id == args['chr']:
		trimmed = record[int(args['start'] -1):args['end']]
# retrieve the id of the gene to use as an output filename
for f in trimmed.features:
	if f.type == 'gene' in f.qualifiers:
		filename = f.qualifiers['locus_tag'][0]
# select directory to export to
os.chdir(args['directory'])
# export to genbank format
SeqIO.write(trimmed,"".join([filename,".gb"]), "genbank")
