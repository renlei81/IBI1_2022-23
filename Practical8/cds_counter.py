import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

stop = re.compile(r'TAA|TAG|TGA')
stop_position = re.finditer(stop,seq)
print(len([u.start() for u in stop_position]))
