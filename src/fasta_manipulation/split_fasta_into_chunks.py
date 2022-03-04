# python3
import os
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input_file", required=True, help="input single or multi-fasta file")
ap.add_argument("-out", "--output_file", required=False, help="output multi-fasta file")
ap.add_argument("-step", "--step_size", required=True, help="step size for chunk creation, type = integer")
ap.add_argument("-win", "--window_size", required=True, help="window size for chunk creation, type = integer")
ap.add_argument("-pro", "--program", type=int, default=1, required=False, help="program output to select 1) 1 multi-fasta file 2) many single-fasta files. Default is 1")
ap.add_argument("-dir", "--directory", required=False, type=str, help="output directory to save the single-fasta files")
args = vars(ap.parse_args())
# main
seqs = []
headers = [] 
chunks = []# setup empty lists
# import multi or single-fasta file
for record in SeqIO.parse(args['input_file'], "fasta"):
	for i in range(0, len(record.seq) - int(args['window_size']) + 1, int(args['step_size'])):
		seqs.append(record.seq[i:i + int(args['window_size'])])
		headers.append('_'.join([record.id,str(i + 1)]))
# export to multi or single-fasta
for (seq, header) in zip(seqs,headers):
	chunks.append(SeqRecord(Seq(str(seq)),id=str(header),description=""))
if args['program']==1:
	SeqIO.write(chunks,args['output_file'], "fasta")
else:
	# set working directory
	os.chdir(args['directory'])
	for chunk in chunks:	
		SeqIO.write(chunk, ''.join([str(chunk.id),".fasta"]), "fasta")
