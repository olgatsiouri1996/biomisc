# python3
import argparse
import sys
# input parameters
ap = argparse.ArgumentParser(description='calculate the probability of an individual carrying a reccesive allele, using the proportion of homozygous reccesive individuals in a given population')
ap.add_argument("-in", "--input", required=True, help="1-column input txt file with the proportion of individuals homozygous for the reccesive allele")
ap.add_argument("-sex", "--sex", required=False, type=str, default='no', help="sex linked for the X chromosome?. Default is no")
ap.add_argument("-out", "--output", required=True, help="2-column tab-seperated output txt file with the probability of containing a reccesive allele and the input column")
args = vars(ap.parse_args())
# convert 1-column txt file to list
with open(args['input'],'r') as f:
    A = f.readlines()
A = [float(x.strip()) for x in A]
# calculate the probability of an individual containing a reccesive allele and output both columns
sys.stdout = open(args['output'],'w')
print('carries_reccesive','proportion_of_homozygous_reccesive',sep='\t',end='\n')
if args['sex'] == 'no':
    for i in A:
        print("%.3f" % round(2*i**0.5-i,3),"%.3f" % round(i,3),sep='\t',end='\n')
else:
    for i in A:
        print("%.3f" % round(2*i*(1-i),3),"%.3f" % round(i,3),sep='\t',end='\n')

sys.stdout.close()
