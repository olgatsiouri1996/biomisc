# julia
using ArgParse
using BioStructures
# input parameters function
function parse_commandline()

    s = ArgParseSettings(description = "input a pdb ids from PDB and subset by selecting the model and chain")
    @add_arg_table s begin
        "--id"
            help = "input pdb ids"
        "--model"
            help = "model to make the pdb file for"
            arg_type = Int
            default = 1
            required = false
        "--chain"
            help = "chain in model to make the pdb file for"    
        "--out"
            help = "output pdb file"
    end
    return parse_args(s)
end

function main()
    parsed_args = parse_commandline()
    println(parsed_args)
# main
    downloadpdb(parsed_args["id"]) do fp
        s = read(fp, PDB)
        subpdb = s[parsed_args["model"]][parsed_args["chain"]]
        writepdb(parsed_args["out"], subpdb)
    end
end

main()