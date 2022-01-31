# python3
import argparse
import itertools
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from dnachisel import *
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa", "--fasta", required=True, help="input multi-fasta file")
ap.add_argument("-org","--organism", required=True, help=" 1-column txt file with organisms to input(use either the names of the genomes avaliable on dnachisel or use the taxid of the organisms in http://www.kazusa.or.jp/codon/)")
ap.add_argument("-opt","--optimized", required=True, help="output multi-fasta file with optimized sequences")
ap.add_argument("-pro", "--program", required=False, type=int, default=1, help="program to choose. 1) pair each taxid to 1 fasta record file, 2) iterate all fasta records with many taxids")
args = vars(ap.parse_args())
# main
cds = [] 
headers = []
optimized_seqs = [] # setup empty lists
# store seqs and ids from coding sequences to lists
for record in SeqIO.parse(args['fasta'], "fasta"):
    cds.append(record.seq)
    headers.append(record.id)
# import file with taxonomy ids and/or organism names
with open(args['organism'], 'r') as f:
    taxids = f.readlines()
taxids = [x.strip() for x in taxids]
# select program
if args['program']==1:
    # iter elements on pairs to codon optimize each sequence to a specific taxid
    for (a, b, c) in itertools.zip_longest(headers, cds, taxids):
        problem = DnaOptimizationProblem(sequence=str(b),
        constraints=[EnforceTranslation()],
        objectives=[CodonOptimize(species= str(c))])
        problem.optimize()
        # add this record to the list
        optimized_seqs.append(SeqRecord(Seq(problem.sequence),id="".join([str(a),"_",str(c)]),description=""))
else:
    # iter all single-fasta files with each taxid 
    for i in taxids:
        # codon optimize using a pair of the below 3 lists
        for (a, b) in zip(headers, cds):
            problem = DnaOptimizationProblem(sequence=str(b),
            constraints=[EnforceTranslation()],
            objectives=[CodonOptimize(species= str(i))])
            problem.optimize()
            # add this record to the list
            optimized_seqs.append(SeqRecord(Seq(problem.sequence),id="".join([str(a),"_",str(i)]),description=""))
# export to fasta
SeqIO.write(optimized_seqs, args['optimized'], "fasta")

