import re
# input sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# define three stop codons to be found
stop = re.compile(r'TAA|TAG|TGA')
#find possible stop codons
stop_position = re.finditer(stop,seq)
# because it used re.finditer, which will not output a list,so just use a for loop to find all start positions and put them in a list
print(len([u.start() for u in stop_position]))
# print the length of the list
