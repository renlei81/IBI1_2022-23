import re
stop_codon = input('input TAA or TAG or TGA:')
input_file = open("D:/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")


output_file = open(f'D:/{stop_codon}_cds_gene.fa','w')
find_gene = ''
find_sequence = ''  
#make two empty strings
for line in input_file:
    line = line.strip() #get the text in the file
    if line.startswith('>'): #judge if the line starts with >, which suggests that it is a line that contains the name
        if find_sequence.endswith(f'{stop_codon}'): # judge if the line ends with the input stop_codon
            output_file.write(f">{find_gene} {len(re.findall(f'{stop_codon}',find_sequence))}\n{find_sequence}\n")#the name, numbers of input stop codon, and the sequence matched
        find_gene = line[1:].split(' ')[0] #split the things by space
        find_sequence = ''
    else:
        find_sequence += line
        
if find_sequence.endswith(f'{stop_codon}'):
    output_file.write(f">{find_gene} {len(re.findall(f'{stop_codon}',find_sequence))}\n{find_sequence}\n")#find the last line

