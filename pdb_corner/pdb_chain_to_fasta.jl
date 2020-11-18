# julia
using ArgParse
using BioStructures
# input parameters function
function parse_commandline()

    s = ArgParseSettings(description = "read a pdb file from PDB and convert it to fasta without the need to download it choosing the model and chain")
    @add_arg_table s begin
        "--pdb"
            help = "input pdb ids"
        "--model"
            help = "model to make the fasta file for"
        "--chain"
            help = "chain in model to make the fasta file for"    
        "--out"
            help = "output fasta file"
    end
    return parse_args(s)
end

function main()
    parsed_args = parse_commandline()
    println(parsed_args)
# main
    downloadpdb(parsed_args["pdb"]) do fp
        s = read(fp, PDB)
        open(parsed_args["out"],"a") do io
            println(io,">",parsed_args["pdb"],"_",parsed_args["chain"],"\n",LongAminoAcidSeq(s[parse(Int, parsed_args["model"])][parsed_args["chain"]], standardselector, gaps=false))
        end
    end
end

main()