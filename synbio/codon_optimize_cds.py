# python3
import argparse
from Bio import SeqIO
from dnachisel import *
import sys
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa", "--fasta", required=True, help="input fasta file")
ap.add_argument("-org","--organism", required=True, help="organism to input(use either the names of the genomes avaliable on dnachisel or use the taxid of the organisms in http://www.kazusa.or.jp/codon/)")
ap.add_argument("-opt","--optimized", required=True, help="optimized genbank file")
args = vars(ap.parse_args())
# main
sys.stdout = open(args['optimized'], 'a')
for record in SeqIO.parse(args['fasta'], "fasta"):
    problem = DnaOptimizationProblem(sequence=str(record.seq),
    objectives=[CodonOptimize(species= args['organism'])])
    problem.optimize()
    print(">"+record.id,problem.sequence, sep='\n')
sys.stdout.close()

