# python3
import argparse
import pandas as pd
import warnings
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input bed file")
ap.add_argument("-out", "--output", required=True, help="output bed file")
ap.add_argument("-fea", "--feature", required=False, default='gene',  type=str, help="specify the pattern to print the lines that have it. Default is \"gene\"")
ap.add_argument("-col", "--column", required=False, default=8, type=int, help="specify the column number to search for the pattern. Default is 8")
args = vars(ap.parse_args())
# main
# ignore warnings
warnings.filterwarnings('ignore')
# fix index for column
feature_col = args['column'] - 1
# import bed with no headers specified
df = pd.read_csv(args['input'], sep= "\t", header=None)
# select the rows containing the feature
bool2 = df.iloc[:, feature_col].str.contains(args['feature']) 
df = df[bool2]
# export
with open(args['output'], 'a') as f:
    f.write(
        df.to_csv(header = False, index = False, sep= "\t", doublequote= False, line_terminator= '\n')
    )


