# python3
import os
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from dnachisel import *
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-org","--organism", required=True, help="organism to input(use either the names of the genomes avaliable on dnachisel or use the taxid of the organisms in http://www.kazusa.or.jp/codon/)")
args = vars(ap.parse_args())
# main
# import each fasta file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
    if filename.endswith(".fa") or filename.endswith(".fasta"):
        record = SeqIO.read(filename, "fasta")
        problem = DnaOptimizationProblem(sequence=str(record.seq),
        constraints=[EnforceTranslation()],
        objectives=[CodonOptimize(species= args['organism'])])
        problem.optimize()
        # create seqRecord with optimized sequence
        optimized_seq=SeqRecord(Seq(problem.sequence),id="".join([record.id,"_",args['organism']]),description="")
        # export to fasta
        SeqIO.write(optimized_seq, "".join([filename.split(".")[0],"_",args['organism'],".fasta"]), "fasta")
