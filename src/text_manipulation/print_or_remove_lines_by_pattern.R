#!/usr/bin/env Rscript
library(glue)
library(stringr)
args = commandArgs(trailingOnly=TRUE)
glue("usage: print_or_remove_lines_by_pattern.R input_txt header_boolean column_name pattern boolean_print_or_remove output_txt")
# main
input_txt <- read.delim(args[1], header= as.logical(args[2]))
filtered_txt <- input_txt[str_detect(input_txt[ ,as.numeric(args[3])], args[4], negate = as.logical(args[5])), ] 
write.table(filtered_txt, file = args[6],quote = FALSE,row.names = FALSE,sep = "\t",eol = "\n")
