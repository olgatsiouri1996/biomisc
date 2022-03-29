# python3
# original code from https://github.com/ssjunnebo/Rosalind/blob/master/spec/spec.py
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input 1-column txt file with numbers")
ap.add_argument("-id", "--id", required=True, type=str, help="fasta header of the output fasta file")
ap.add_argument("-out", "--output", required=True, help="output fasta file with the protein sequence")
args = vars(ap.parse_args())
# main
L = [float(line) for line in open(args['input'],'r')]

mass_table = {'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841,'G':57.02146,'H':137.05891,'I':113.08406,'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276,'Q':128.05858,'R':156.10111,'S':87.03203,'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06333}

aa_masses = []
for i in range(len(L) - 1):
    aa_mass = round(L[i + 1] - L[i], 4)
    aa_masses.append(aa_mass)

rnd_mass_table = {}
for k, v in mass_table.items():
    rnd_mass_table[round(v, 4)] = k

prot = ''
for aa in aa_masses:
    prot += rnd_mass_table[aa]

record = SeqRecord(Seq(prot),id=args['id'],description="")
SeqIO.write(record, args['output'],"fasta")


