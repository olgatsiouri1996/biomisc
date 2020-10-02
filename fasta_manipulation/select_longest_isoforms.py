# python 3
from __future__ import print_function
import sys
import argparse
from Bio import SeqIO
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input fasta")
ap.add_argument("-n", "--number", required=True, help="number of longest isoforms to write")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
args = vars(ap.parse_args())
# main
def main():
    
    last_gene = None
    transcripts = []

    for record in SeqIO.parse(args['input'], "fasta"):
        gene = record.id.split(".")[0]

        if last_gene is None:
            last_gene = gene

        if last_gene == gene:
            transcripts.append(record)
        else:
            print_longest_transcripts(transcripts, int(args['number']))
            last_gene = gene
            transcripts = [record]

    print_longest_transcripts(transcripts, int(args['number']))


def print_longest_transcripts(transcripts, number):
    longest = sorted(transcripts, key=lambda x: len(x.seq), reverse=True)
    sys.stdout = open(args['output'], 'a')    
    for record in longest[:number]:
        print(">"+record.id, record.seq, sep="\n")
    sys.stdout.close()

if __name__ == '__main__':
    main()
    