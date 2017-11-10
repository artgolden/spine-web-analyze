'''Searching substring in string of nucleotides'''
# from bitstring import BitArray
nucleotides = 'AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCG'
pattern = 'AGGTCT'
length = len(pattern)



def letter_to_bin(letter):
	
	
	return b

def str_to_num(line):
	
	n = 3
	for i in range(len(line) - 1, -1, -1):
		print bin(n)
		if line[i] == 'A':
			n = n << 2
			n += 0
		elif line[i] == 'C':
			n = n << 2  
			n += 1 
		elif line[i] == 'T':
			n = n << 2  
			n += 2 
		elif line[i] == 'G':
			n = n << 2  
			n += 3 
		else:
			print "Error: Wrong letter!"
			break
	return n

def compare_numbers(matrix, frame):
	if matrix == frame:
		return True
	else:
		return False

def move_frame(pattern, nucleotides):
	pass
	matrix = str_to_num(pattern)
	frame = str_to_num(nucleotides[:len(pattern)])
	found = False
	for i in range(len(nucleotides) - len(pattern)):
		if compare_numbers(matrix, frame):
			found = True
		frame = frame >> 2
		add = 0b1001 << length
		letter = 
		frame += add

		frame += 



print bin(str_to_num(pattern))
