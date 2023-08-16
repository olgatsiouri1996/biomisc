# python3
import argparse
import os
from pyfaidx import Fasta
import textwrap
# input parameters
ap = argparse.ArgumentParser(description="use a txt file with fasta identifiers to extract or remove sequences from fasta file")
ap.add_argument("-in", "--input", required=True,  help="input multi-fasta file")
ap.add_argument("-ids", "--ids", required=True,  help="1 or multiple column tab seperated file with no column names, with fasta identifiers in the 1st column to retrieve the output fasta sequences. The 2nd column can contain the groupname the identifier belongs, to split into many multi-fasta files 1 per group name")
ap.add_argument("-act", "--action",type=str, default='extract', required=False, choices=['extract','remove'], widget='Dropdown', help="choose to extract or remove sequences. Default extract")
ap.add_argument("-ty", "--type", type=int, default=1, choices=range(1, 10),
                        help="Choose output type:\n"
                             "1: 1 multi-fasta file\n"
                             "2: many single-fasta files\n"
                             "3: many multi-fasta files 1 per group\n"
                             "4: many multi-fasta files by number of records\n"
                             "5: 2-column txt file(id,seq)\n"
                             "6: 3-column txt file(id,description,seq)\n"
                             "7: 3-column txt file(id,full_fasta_header,seq)\n"
                             "8: 2-column txt file(id,description)\n"
                             "9: 1-column txt file(id). Default is 1")
ap.add_argument("-out", "--output", required=False, help="output multi-fasta or a 1-column or a 2-column or a 3-column txt file")
ap.add_argument("-dir", "--directory", required=False, type=str, default='.', help="output directory to save many single- or multi-fasta files. Default is the current directory")
ap.add_argument("-prefix", "--prefix",type=str,  required=False, help="output file prefix when choosing the program type: many multi-fasta files by number of records")
ap.add_argument("-num", "--number",type=int, required=False, help="number of fasta records to output per file when choosing the program type: many multi-fasta files by number of records")
args = vars(ap.parse_args())
# main
# import the txt file with headers you want to extract the sequence from the input fasta
headers = (str(line.rstrip()).split()[0] for line in open(args['ids']))
# import fasta file
features = Fasta(args['input'])
# choose to remove sequences
if 'remove' in args['action']:
    # collect ids of import fasta file
    keyslist = (features.keys())
    # remove those that exist in the headers generator
    final_keys = (set(keyslist).difference(headers))
else:
    final_keys = headers
# choose program
program = args['type']
match program:
    case 1:
        # export to 1 multi-fasta
        with  open(args['output'], 'w') as f:
            for key in final_keys:
                f.write(f'>{str(features[str(key)].long_name).rstrip()}\n{textwrap.fill(features[str(key)][:].seq, width=60)}\n')                
    case 2:
        # extract many sigle-fasta files
        os.chdir(args['directory'])
        for key in final_keys:
            with open(str(key)+".fasta", 'w') as f:
                f.write(f'>{str(features[str(key)].long_name).rstrip()}\n{textwrap.fill(features[str(key)][:].seq, width=60)}\n')
    case 3:
        # create a dictionary with identifier and group
        identifier_to_group = {}
        groups = (str(line.rstrip()).split()[1] for line in open(args['ids']))
        for (identifier, group) in zip(headers, groups):
            identifier_to_group[identifier] = group
        # populate group_to_sequences dictionary
        group_to_sequences = {}
        for identifier, group in identifier_to_group.items():
            if group not in group_to_sequences:
                group_to_sequences[group] = []
            sequence = textwrap.fill(features[str(identifier)][:].seq, width=60)
            description = features[str(identifier)].long_name
            group_to_sequences[group].append((description, sequence))
        # write sequences to group-specific output files
        os.chdir(args['directory'])
        for group, sequences in group_to_sequences.items():
            output_file_name = f"{group}.fasta"
            with open(output_file_name, "w") as output_file:
                for description, sequence in sequences:
                    output_file.write(f">{description}\n{sequence}\n")
    case 4:   
        split_lists = [list(final_keys)[x:x+args['number']] for x in range(0, len(list(final_keys)), args['number'])]
        # Extract many multi-fasta files
        for count, lis in enumerate(split_lists, 1):
            output_file = os.path.join(args['directory'], f"{args['prefix']}_part{count}.fasta")
            with open(output_file, 'w') as output:
                for key in lis:
                    header = str(features[str(key)].long_name).rstrip()
                    output.write(f">{header}\n")
                    seq = str(features[str(key)][:].seq).rstrip()
                    wrapped_seq = textwrap.fill(seq, width=60)
                    output.write(wrapped_seq + '\n')
    case 5:                        
        # iterate input headers to extract sequences and export as 2 column txt
        with  open(args['output'], 'w') as f:
            f.write(f'{"id"}\t{"seq"}\n')
            for key in final_keys:
                f.write(f'{str(key)}\t{features[str(key)][:].seq}\n')
    case 6:
        # iterate input headers to extract sequences and export as 3 column txt
        with  open(args['output'], 'w') as f:
            f.write(f'{"id"}\t{"description"}\t{"seq"}\n')
            for key in final_keys:
                try:
                    f.write(f'{str(key)}\t{str(str(features[str(key)].long_name).rstrip()).split(" ",1)[1]}\t{features[str(key)][:].seq}\n')
                except IndexError:
                    f.write(f'{str(key)}\t{""}\t{features[str(key)][:].seq}\n')
    case 7:           
        # iterate input headers to extract sequences and export as 3 column txt
        with  open(args['output'], 'w') as f:
            f.write(f'{"id"}\t{"full_fasta_header"}\t{"seq"}\n')
            for key in final_keys:
                f.write(f'{str(key)}\t{str(features[str(key)].long_name).rstrip()}\t{features[str(key)][:].seq}\n')
    case 8:
        # iterate input headers to extract sequences and export as 2 column txt
        with  open(args['output'], 'w') as f:
            f.write(f'{"id"}\t{"description"}\n')
            for key in final_keys:
                try:
                    f.write(f'{str(key)}\t{str(str(features[str(key)].long_name).rstrip()).split(" ",1)[1]}\n')
                except IndexError:
                    f.write(f'{str(key)}\t{""}\n')
    case 9:
        # iterate input headers to extract sequences and export as 1-column txt
        with  open(args['output'], 'w') as f:
            f.write(f'{"id"}\n')
            for key in final_keys:
                f.write(f'{str(key)}\n')

