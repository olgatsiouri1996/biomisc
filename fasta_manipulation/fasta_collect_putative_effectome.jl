# julia
using FASTX
# main
print("collect proteins with length < 300 aa\nusage: julia fasta_collect_putative_effectome.jl input_fasta output_fasta")
reader = open(FASTA.Reader,ARGS[1])
open(ARGS[2],"a") do io
    for record in reader
        if length(FASTA.sequence(record)) < 300
            println(io,record)
        end
    end
    close(reader)
end
