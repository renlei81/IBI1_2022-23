def is_protein_coding(dna_sequence):
    dna_sequence = dna_sequence.upper()
    start_codon = 'ATG'
    stop_codon = 'TGA'
    total_length = len(dna_sequence) #store the length of the DNA
    start_index = dna_sequence.find(start_codon)
    stop_index = dna_sequence.rfind(stop_codon)

    if start_index == -1 or stop_index == -1:#judge if there are the stop or start factors
        return 0, 'unclear'

    coding_length = stop_index - start_index + len(stop_codon)# the length of the coding sequence in the dna
    coding_percentage = coding_length / total_length

    if coding_percentage > 0.5: # calculate the percentage of the coding sequence in the dna
        return coding_percentage * 100, 'protein-coding' #define the types
    elif coding_percentage < 0.1:
        return coding_percentage * 100, 'non-coding'
    else:
        return coding_percentage * 100, 'unclear'
