def is_protein_coding(dna_sequence):
    dna_sequence = dna_sequence.upper()
    start_codon = 'ATG'
    stop_codon = 'TGA'
    total_length = len(dna_sequence)
    start_index = dna_sequence.find(start_codon)
    stop_index = dna_sequence.rfind(stop_codon)

    if start_index == -1 or stop_index == -1:
        return 0, 'unclear'

    coding_length = stop_index - start_index + len(stop_codon)
    coding_percentage = coding_length / total_length

    if coding_percentage > 0.5:
        return coding_percentage * 100, 'protein-coding'
    elif coding_percentage < 0.1:
        return coding_percentage * 100, 'non-coding'
    else:
        return coding_percentage * 100, 'unclear'
