# python3
import argparse
import os
import sys
from pyfaidx import Fasta
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=False, help="input multi-fasta file")
ap.add_argument("-num", "--number", required=True, type=int, help="number of fasta records per output fasta file(you can put any number you want as it makes sure the the remainig fasta records will be written to a seperate file as well)")
ap.add_argument("-dir", "--directory", required=False, type=str,  help="directory with multi-fasta files")
ap.add_argument("-pro", "--program", required=False, type=int, default=1,  help="program to choose: 1) split 1 multi-fasta file to many, 2) split many multi-fasta files to many. Default is 1")
args = vars(ap.parse_args())
# main
# create function to split the input sequence based on a specific number of characters(60)
def split_every_60(s): return [str(s)[i:i+60] for i in range(0,len(str(s)),60)]
# choose program
if args['program'] == 1:
    # import fasta file
    features = Fasta(args['input'])
    # initial count of files
    count = 0
    # split list
    keyslist = list(features.keys())
    split_lists = [keyslist[x:x+args['number']] for x in range(0, len(keyslist), args['number'])]
    # extract many sigle-fasta files
    for lis in split_lists:
        count = count + 1
        sys.stdout = open(''.join([str(args['input']).split('.fa')[0],"_","part",str(count),".fasta"]), 'a')
        for key in lis:
            print(''.join([">",features[str(key)].long_name]).replace('\r',''))
            print('\n'.join(split_every_60(features[str(key)][:].seq)))
        sys.stdout.close()
else:
    # import multi-fasta from current directory
    for filename in sorted(os.listdir(os.chdir(args['directory']))):
        if filename.endswith(".fa") or filename.endswith(".fasta"):
            # import fasta file
            features = Fasta(filename)
            # initial count of files
            count = 0
            # split list
            keyslist = list(features.keys())
            split_lists = [keyslist[x:x+args['number']] for x in range(0, len(keyslist), args['number'])]
            # extract many sigle-fasta files
            for lis in split_lists:
                count = count + 1
                sys.stdout = open(''.join([str(filename).split('.fa')[0],"_","part",str(count),".fasta"]), 'a')
                for key in lis:
                    print(''.join([">",features[str(key)].long_name]).replace('\r',''))
                    print('\n'.join(split_every_60(features[str(key)][:].seq)))
                sys.stdout.close()
            del features; keyslist.clear(); split_lists.clear()

