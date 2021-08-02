# python3
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from dnachisel import *
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-fa", "--fasta", required=True, help="input single fasta with coding sequence file")
ap.add_argument("-prot", "--proteins", required=True, help="input multi fasta file with protein sequences")
ap.add_argument("-org","--organism", required=True, help="organism to input(use either the names of the genomes avaliable on dnachisel or use the taxid of the organisms in http://www.kazusa.or.jp/codon/)")
ap.add_argument("-opt","--optimized", required=True, help="optimized fasta file")
args = vars(ap.parse_args())
# main
cds = SeqIO.read(args["fasta"], "fasta")
optimized_seqs = [] # setup an empty list
for record in SeqIO.parse(args['proteins'], "fasta"):
    problem = DnaOptimizationProblem(sequence=str(cds.seq),
    constraints=[EnforceTranslation(translation=str(record.seq))],
    objectives=[CodonOptimize(species= args['organism'])])
    problem.optimize()
    # add this record to the list
    optimized_seqs.append(SeqRecord(Seq(problem.sequence),id=record.id,description=""))
# export to fasta
SeqIO.write(optimized_seqs, args['optimized'], "fasta")
