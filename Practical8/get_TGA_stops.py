import re

input_file = open("D:/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
output_file = open('D:/TGA_genes.fa','w')


find_gene = ''
find_sequence = ''           
for line in input_file:
    line = line.strip()
    if line.startswith('>'):
        if find_sequence.endswith('TGA'):
            output_file.write(f">{find_gene}\n{find_sequence}\n")
        find_gene = line[1:].split(' ')[0]
        find_sequence = ''
    else:
        find_sequence += line
        
if find_sequence.endswith('TGA'):
    output_file.write(f">{find_gene}\n{find_sequence}\n")
    
    
    
    
input_file.close()
output_file.close()
