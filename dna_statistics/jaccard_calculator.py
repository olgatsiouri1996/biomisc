import argparse
from Bio import SeqIO
import matplotlib
from matplotlib_venn import venn2
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-seq1", "--seq1", required=True, help="first fasta to import")
ap.add_argument("-seq2", "--seq2", required=True, help="second fasta to import")
ap.add_argument("-step", "--step", required=True, help="step size to split fasta, type = int")
ap.add_argument("-win", "--window", required=True, help="window size of splitted subsets, type = int")
ap.add_argument("-plot", "--plot", required=True, help="export venn diagram to file")
ap.add_argument("-dpi", "--dpi", required=True, help="dpi of exported plot")
args = vars(ap.parse_args())
# calculate similarity
def jaccard_similarity(a, b):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))
    union = len(a.union(b))

    return intersection / union
# calculate containment
def jaccard_containment(a, b):
    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))

    return intersection / len(a)
# main
seq1 = []
for record in SeqIO.parse(args['seq1'], "fasta"):
    for i in range(0, len(record.seq) - int(args['window']) + 1, int(args['step'])):
        seq1.append(record.seq[i:i + int(args['window'])])
seq2 = []
for record in SeqIO.parse(args['seq2'], "fasta"):
    for i in range(0, len(record.seq) - int(args['window']) + 1, int(args['step'])):
        seq2.append(record.seq[i:i + int(args['window'])])

print("seq1 vs seq2", jaccard_similarity(seq1, seq2))
print("seq2 vs seq1", jaccard_similarity(seq2, seq1))
print("seq1 vs seq2", jaccard_containment(seq1, seq2))
print("seq2 vs seq1", jaccard_containment(seq2, seq1))
plt = venn2([set(seq1), set(seq2)],('Seq1','Seq2'))
matplotlib.pyplot.savefig(args['plot'], dpi=int(args['dpi']))