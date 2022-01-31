# julia
using FASTX
# main
print("print the full header line from fasta file\nusage: julia fasta_to_header.jl input_fasta output_txt")
reader = open(FASTA.Reader,ARGS[1])
open(ARGS[2],"a") do io
   for record in reader
      println(io,FASTA.identifier(record),"\t",FASTA.description(record))
   end
end
close(reader)
