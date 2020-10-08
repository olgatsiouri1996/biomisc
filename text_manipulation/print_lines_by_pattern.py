# python3
import argparse
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input txt/tsv file")
ap.add_argument("-out", "--output", required=True, help="output txt/tsv file")
ap.add_argument("-p", "--pattern", required=True, help="specify the pattern to print the lines that have it(put the pattern into doublequotes)")
ap.add_argument("-c", "--column", required=True, help="specify the column number to search for the pattern(starts from 0)")
args = vars(ap.parse_args())
# main
df = pd.read_csv(args['input'], sep= "\t", encoding='latin-1')
df = df.fillna("")
bool2 = df.iloc[:, int(args['column'])].str.contains(args['pattern']) 
df = df[bool2]
# export
with open(args['output'], 'a') as f:
    f.write(
        df.to_csv(header = True, index = False, sep= "\t", doublequote= False, line_terminator= '\n')
    )


