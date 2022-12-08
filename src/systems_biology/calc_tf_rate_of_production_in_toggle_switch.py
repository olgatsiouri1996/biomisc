# python3
import argparse
import sys
# input parameters
ap = argparse.ArgumentParser(description='calculate transcriptional repressor rate of production using tf concetrations in a toggle switch')
ap.add_argument("-in", "--input", required=True, help="2-column input txt file with the concetrations of the 2 repressors(no headers)")
ap.add_argument("-alpha1", "--alpha1", required=True, type=float, help="effective rate of synthesis of repressor 1")
ap.add_argument("-alpha2", "--alpha2", required=True, type=float, help="effective rate of synthesis of repressor 2")
ap.add_argument("-beta", "--beta", required=True, type=int, help="cooperativity of repression of promoter 2")
ap.add_argument("-gamma", "--gamma", required=True, type=int, help="cooperativity of repression of promoter 1")
ap.add_argument("-out", "--output", required=True, help="4-column tab-seperated output txt file with the rate of tf productions and the input columns")
args = vars(ap.parse_args())
# inport variables
b = args['beta']
g = args['gamma']
a1 = args['alpha1']
a2 = args['alpha2']
# create function to calc the production rate of promoter 1
def u_production_rate(s):
    return a1/(1 + s**b)
 # create function to calc the production rate of promoter 2
def v_production_rate(s):
    return a2/(1 + s**g)
# convert 2-column txt file to 2 generators 1 per column
tf1 = (float(str(line.rstrip()).split()[0]) for line in open(args['input']))
tf2 = (float(str(line.rstrip()).split()[1]) for line in open(args['input']))
# calculate the protein production rates and export to file
sys.stdout = open(args['output'],'w')
print('rate_of_protein1_production','rate_of_protein2_production','protein1_concertration','protein2_concertration',sep='\t',end='\n')
for (c1,c2) in zip(tf1,tf2):
    print("%.3f" % round(u_production_rate(c1),3),"%.3f" % round(v_production_rate(c2),3),"%.3f" % round(c1,3),"%.3f" % round(c2,3),sep='\t',end='\n')
sys.stdout.close()
