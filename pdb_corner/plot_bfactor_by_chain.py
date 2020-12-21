# python3
import argparse
from biopandas.pdb import PandasPdb
import matplotlib
import matplotlib.pyplot as plt
# input parameters
ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input pdb file")
ap.add_argument("-chain", "--chain", required=True, help="chain from pdb file to select")
ap.add_argument("-col", "--col", required=True, help="colour of line in plot(write in '' or "" you can use hex colour codes)")
ap.add_argument("-plot", "--plot", required=False, help="export plot to file")
ap.add_argument("-dpi", "--dpi", default= 300, required=False, help="dpi of exported plot")
ap.add_argument("-type", "--type", required=True, help="type of plot file(e.g png etc)")
args = vars(ap.parse_args())
# main
ppdb = PandasPdb()
ppdb.read_pdb(args['input'])
ppdb.df['ATOM'] = ppdb.df['ATOM'][ppdb.df['ATOM']['chain_id'] == args['chain']]
# export figure
ppdb.df['ATOM']['b_factor'].plot(kind='line', color= args['col'])
plt.title('B-Factors Along the Amino Acid Chain')
plt.xlabel('Atom Number')
plt.ylabel('B-factor in $A^2$')
matplotlib.pyplot.savefig(args['plot'], dpi=int(args['dpi']), format=args['type'])
