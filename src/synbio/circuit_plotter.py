# python3
import argparse
import synbiopython
import synbiopython.genbabel as stdgen
# imput parameters

ap = argparse.ArgumentParser()
ap.add_argument("-in", "--input", required=True, help="input circuit components")
ap.add_argument("-reg", "--regulations", required=True, help="regulations of circuit components(e.g activation)")
ap.add_argument("-plot", "--plot", required=True, help="file to save the circuit plot")
args = vars(ap.parse_args())
# main
simplot = stdgen.SimpleDNAplot()
Input = args['input']
Regulations = args['regulations']
maxdnalength, figure = simplot.plot_circuit(Input, Regulations, args['plot'])

