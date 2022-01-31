import argparse
from Bio import SeqIO
import matplotlib
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-seq1", "--seq1", required=True, help="first fasta to import")
ap.add_argument("-name1", "--name1", required=True, help="name of seq1's sequence/organism")
ap.add_argument("-col1", "--col1", required=True, help="colour of seq1's subset in venn")
ap.add_argument("-seq2", "--seq2", required=True, help="second fasta to import")
ap.add_argument("-name2", "--name2", required=True, help="name of seq2's sequence/organism")
ap.add_argument("-col2", "--col2", required=True, help="colour of seq2's subset in venn")
ap.add_argument("-step", "--step", required=True, help="step size to split fasta, type = int")
ap.add_argument("-win", "--window", required=True, help="window size of splitted subsets, type = int")
ap.add_argument("-plot", "--plot", required=True, help="export venn diagram to file")
ap.add_argument("-dpi", "--dpi", required=True, help="dpi of exported plot")
ap.add_argument("-alpha", "--alpha", required=True, help="plot opacity")
ap.add_argument("-width", "--width", required=True, help="plot width")
ap.add_argument("-tall", "--tall", required=True, help="plot height")
ap.add_argument("-type", "--type", required=True, help="type of plot file(e.g png etc)")
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

print("seq1 vs seq2 jaccard similarity", jaccard_similarity(seq1, seq2))
print("seq2 vs seq1 jaccard similarity", jaccard_similarity(seq2, seq1))
print("seq1 vs seq2 jaccard containment", jaccard_containment(seq1, seq2))
print("seq2 vs seq1 jaccard containment", jaccard_containment(seq2, seq1))
plt.figure(figsize=(float(args['width']), float(args['tall'])))
v = venn2([set(seq1), set(seq2)],(args['name1'], args['name2']), (args['col1'], args['col2']), alpha = float(args['alpha']))
matplotlib.pyplot.savefig(args['plot'], dpi=int(args['dpi']), format=args['type'])