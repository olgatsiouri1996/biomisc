# python3
import argparse
import itertools
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from dnachisel import *
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa", "--fasta", required=True, help="input multi fasta file with coding sequences")
ap.add_argument("-prot", "--proteins", required=True, help="input multi fasta file with protein sequences")
ap.add_argument("-org","--organism", required=True, help="1-column txt file with organisms to input(use either the names of the genomes avaliable on dnachisel or use the taxid of the organisms in http://www.kazusa.or.jp/codon/)")
ap.add_argument("-opt","--optimized", required=True, help="optimized fasta file")
args = vars(ap.parse_args())
# main
# import multi fasta and add coding sequences to list
cds = []
for record in SeqIO.parse(args["fasta"], "fasta"):
    cds.append(record.seq)
# import file with taxonomy ids and/or organism names
with open(args['organism'], 'r') as f:
    taxids = f.readlines()
taxids = [x.strip() for x in taxids] 
# add protein sequences and ids to list
prot_seqs = []
prot_ids = []
for record in SeqIO.parse(args['proteins'], "fasta"):
    prot_seqs.append(record.seq)
    prot_ids.append(record.id)
# iterate for 4 items of each list
optimized_seqs = [] # setup an empty list
for (a, b, c, d) in itertools.zip_longest(cds, prot_seqs, prot_ids, taxids):
    problem = DnaOptimizationProblem(sequence=str(a),
    constraints=[EnforceTranslation(translation=str(b))],
    objectives=[CodonOptimize(species= str(d))
    problem.optimize()
    # add this record to the list
    optimized_seqs.append(SeqRecord(Seq(problem.sequence),id=str(c),description=""))
# export to fasta
SeqIO.write(optimized_seqs, args['optimized'], "fasta")
