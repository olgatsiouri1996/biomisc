# python3
import os
import argparse
import itertools
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from dnachisel import *
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-org","--organism", required=True, help=" 1-column txt file with organisms to input(use either the names of the genomes avaliable on dnachisel or use the taxid of the organisms in http://www.kazusa.or.jp/codon/)")
ap.add_argument("-pro", "--program", required=False, type=int, default=1, help="program to choose. 1) pair each taxid to 1 fasta file, 2) iterate all fasta with many taxids")
args = vars(ap.parse_args())
# main
cds = [] 
headers = []
names = [] # setup empty lists
# store seqs and ids from coding sequences to lists
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        record = SeqIO.read(filename, "fasta")
        cds.append(record.seq)
        headers.append(record.id)
        names.append(filename.split(".")[0])
# import file with taxonomy ids and/or organism names
with open(args['organism'], 'r') as f:
    taxids = f.readlines()
taxids = [x.strip() for x in taxids]
# select program
if args['program']==1:
    # iter elements on pairs to codon optimize each sequence to a specific taxid
    for (a, b, c, d) in itertools.zip_longest(headers, cds, taxids, names):
        problem = DnaOptimizationProblem(sequence=str(b),
        constraints=[EnforceTranslation()],
        objectives=[CodonOptimize(species= str(c))])
        problem.optimize()
        # add this record to the list
        optimized_seq=SeqRecord(Seq(problem.sequence),id="".join([str(a),"_",str(c)]),description="")
        # export to fasta
        SeqIO.write(optimized_seq, "".join([str(d),"_",str(c),".fasta"]), "fasta")
else:
    # iter all single-fasta files with each taxid 
    for i in taxids:
        # codon optimize using a pair of the below 3 lists
        for (a, b, c) in zip(headers, cds, names):
            problem = DnaOptimizationProblem(sequence=str(b),
            constraints=[EnforceTranslation()],
            objectives=[CodonOptimize(species= str(i))])
            problem.optimize()
            # add this record to the list
            optimized_seq=SeqRecord(Seq(problem.sequence),id="".join([str(a),"_",str(i)]),description="")
            # export to fasta
            SeqIO.write(optimized_seq, "".join([str(c),"_",str(i),".fasta"]), "fasta")

