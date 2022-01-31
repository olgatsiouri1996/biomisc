# python3
import argparse
import sys
import COG
from more_itertools import flatten
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input txt file with each COG in each line")
ap.add_argument("-out", "--output", required=True, help="output tab seperated txt file with each COGs and their functional category descriptions")
args = vars(ap.parse_args())
# main
sys.stdout = open(args['output'], 'a')    
with open(args['input'], 'r') as f:
    for line in f:
        spl = line.split()
        func_tuple = COG.cat_from_letter(spl[0])
        func_tuple_flat = list(flatten(func_tuple))
        annot = list(flatten(func_tuple_flat))
        print('\t'.join(annot))
sys.stdout.close()
