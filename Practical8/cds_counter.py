import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA' #imput the possible sequence

stop = re.compile(r'TAA|TAG|TGA') #possible stop possitions

stop_position = re.finditer(stop,seq) #find stop codon in the seq

print(len([u.start() for u in stop_position])) 
# print the length of the list, which contains all results of the finditer
