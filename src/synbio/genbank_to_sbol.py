# python3
import argparse
import synbiopython
import synbiopython.genbabel as stdgen
# imput parameters
ap = argparse.ArgumentParser()
ap.add_argument("-gb", "--genbank", required=True, help="input genbank file")
ap.add_argument("-sbol", "--sbol", required=True, help="outpul sbol file")
args = vars(ap.parse_args())
# main
stdconv = stdgen.GenSBOLconv()
uri_Prefix_igb = 'http://synbiohub.org/public/igem'
stdconv.run_sbolvalidator(args['genbank'],'SBOL2', uri_Prefix_igb, outputfile = args['sbol'])
