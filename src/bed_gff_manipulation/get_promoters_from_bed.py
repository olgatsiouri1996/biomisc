# python3
import argparse
import sys
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-bed", "--bed", required=True, help="input bed file with genes as the only features(made with bedops, every feature in the \'.gff\' or \'.gff3\' file should have an \'ID\' tag in the \'attributes\' column)")
ap.add_argument("-in", "--input", required=True, help="input fasta file")
ap.add_argument("-out", "--output", required=True, help="output fasta file")
ap.add_argument("-pro", "--promoter", required=False, default=2000, type=int, help="promoter length. Default is 2000")
args = vars(ap.parse_args())
# main
# setup empty lists
chrom = []
start = []
end = []
ids = []
strand = []
# import bed 
with open(args['bed'], 'r') as f:
    for line in f:
        # convert each column to list
        chrom.append(line.split()[0])
        start.append(line.split()[1])
        end.append(line.split()[2])
        ids.append(line.split()[3])
        strand.append(line.split()[5])
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# import fasta file
features = Fasta(args['input'])
# iterate all below lists in pairs
sys.stdout = open(args['output'], 'w')
for (a, b, c, d, e) in zip(ids, chrom, start, end, strand):
    if str(e) == "+":
        if int(c) - args['promoter'] - 1 <= 0:
            print(''.join([">",str(a)," ",str(b),":",str(1),"-",str(c)]).replace('\r', ''))
            print('\n'.join(split_every_60(features[str(b)][:int(c)].seq)))
        else:
            print(''.join([">",str(a)," ",str(b),":",str(int(c) - args['promoter']),"-",str(c)]).replace('\r', ''))
            print('\n'.join(split_every_60(features[str(b)][int(int(c) - args['promoter'] - 1):int(c)].seq)))
    else:
        if int(d) + args['promoter'] >= features[str(b)][:].end:
            print(''.join([">",str(a)," ",str(b),":",str(d),"-",str(features[str(b)][:].end)," ","reverse complement"]).replace('\r', ''))
            print('\n'.join(split_every_60(features[str(b)][int(d):int(features[str(b)][:].end)].reverse.complement.seq)))
        else:
            print(''.join([">",str(a)," ",str(b),":",str(d),"-",str(int(d) + args['promoter'])," ","reverse complement"]).replace('\r', ''))
            print('\n'.join(split_every_60(features[str(b)][int(d):int(int(d) + args['promoter'])].reverse.complement.seq)))
sys.stdout.close()

