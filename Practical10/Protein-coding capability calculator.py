import re
def protein_coding(dna_sequence):
    dna_sequence = dna_sequence.upper()
    start_codon = r'ATG'
    stop_codon = r'TGA'
    total_length = len(dna_sequence) #store the length of the DNA
    start_index = dna_sequence.find(start_codon,re.I)#find start codon in the dna sequence
    stop_index = dna_sequence.rfind(stop_codon,re.I)#find stop codon in the dna sequence
    # re.I is to recognize both upper and lower cases

    if start_index == -1 or stop_index == -1:#judge if there are the stop or start factors
        return 0, 'unclear'

    coding_length = stop_index - start_index + len(stop_codon)# the length of the coding sequence in the dna
    coding_percentage = 100*coding_length / total_length 

    if coding_percentage > 0.5: # calculate the percentage of the coding sequence in the dna
        return f'{coding_percentage}%', 'protein-coding' #define the types
    elif coding_percentage < 0.1:
        return f'{coding_percentage}%', 'non-coding'
    else:
        return f'{coding_percentage}%', 'unclear'
    
print(protein_coding('aaaaatGaaaatGAa')) 
# ('66.66666666666667%', 'protein-coding')
