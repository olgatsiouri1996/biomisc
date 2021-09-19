# python3
import os
from dnachisel import *
# main
# import each genbank file from the working directory
for filename in sorted(os.listdir(str(os.getcwd()))):
	if filename.endswith(".gb") or filename.endswith(".gbk"):
# optimize the sequence from each file
		problem = DnaOptimizationProblem.from_record(filename)
		problem.resolve_constraints()
		problem.optimize()
# create biopython type sequence record from the optimized sequence and export to genbank
		problem.to_record(filepath= "".join([filename.split(".")[0],"_opt",".gb"]), with_sequence_edits=False)
