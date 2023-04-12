import re

input_file = open("D:/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
output_file = open('D:/TGA_genes.fa','w')


find_gene = ''
find_sequence = ''           
#make two empty strings
for line in input_file:
    line = line.strip()#get the text in the file
    if line.startswith('>'): #judge if the line starts with >, which suggests that it is a line that contains the name
        if find_sequence.endswith('TGA'): # judge if the line ends with the TGA
            output_file.write(f">{find_gene}\n{find_sequence}\n")
        find_gene = line[1:].split(' ')[0]#split the things by space
        find_sequence = ''
    else:
        find_sequence += line
        
if find_sequence.endswith('TGA'):
    output_file.write(f">{find_gene}\n{find_sequence}\n")
#find the last line
    
    
    
input_file.close()
output_file.close()
