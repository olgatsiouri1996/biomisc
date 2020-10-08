# python3
import argparse
import pandas as pd
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-tab1", "--table1", required=True, help=" input txt file")
ap.add_argument("-out", "--output", required=True, help="output txt file")
ap.add_argument("-tab2", "--table2", required=True, help="txt file to not match")
ap.add_argument("-header1", "--header1", required=True, help="txt header to select data for merge")
ap.add_argument("-header2", "--header2", required=True, help="txt header from table2 to select the non intersected table1 lines")
args = vars(ap.parse_args())
# main
df1 = pd.read_csv(args['table1'], sep= "\t")
df1 = df1.fillna("")
df2 = pd.read_csv(args['table2'], sep= "\t")
df2 = df2.fillna("")
df_merge_col = pd.merge(df1, df2, on= args['header1'], how='left')
df_merge_col = df_merge_col[df_merge_col[args['header2']].isnull()]
# export
with open(args['output'], 'a') as f:
    f.write(
        df_merge_col.to_csv(header = True, index = False, sep= "\t", doublequote= False, line_terminator= '\n')
    )

