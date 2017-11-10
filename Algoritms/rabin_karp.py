'''Searching substring in string of nucleotides'''
import timeit
nucleotides = 'AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGAGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAATGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCTGGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGAGGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAGATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGACGCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGGGTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGCAGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGCTCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC'
pattern1 = 'GGG'
pattern2 = 'GGGTCTGGGTCT'
pattern3 = 'GGGGTTCATGGGGGTTCATGGGGGTTCATG'
pattern4 = 'GGGGTTCATGTGACTCAGTAGGGGTTCATGTGACTCAGTA'




def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def letter_to_bin(letter):
	b = 0
	if letter == 'A':
		b += 0
	elif letter == 'C':
		b += 1 
	elif letter == 'T':
		b += 2 
	elif letter == 'G':
		b += 3 
	else:
		print "Error: Wrong letter!"
		quit(1)
	return b

def str_to_num(line):
	
	n = 3
	for i in range(len(line) - 1, -1, -1):
		# print bin(n)
		n = n << 2
		n += letter_to_bin(line[i])
	return n

def compare_numbers(matrix, frame):
	if matrix == frame:
		return True
	else:
		return False

def move_frame(pattern, nucleotides, length):
	matrix = str_to_num(pattern)
	frame = str_to_num(nucleotides[:len(pattern)])
	found = False
	for i in range(6, len(nucleotides) - len(pattern)):
		if compare_numbers(matrix, frame):
			found = True
			# print "Pattern is in array:", found
			# quit(0)
		frame = frame >> 2
		# print bin(frame), "frame"
		add = 0b1001 << (length- 1) * 2 
		# print bin(add), "add"
		letter = letter_to_bin(nucleotides[i])
		letter = letter << (length - 1) * 2
		frame += add
		# print bin(frame), "frame", nucleotides[i]
		frame += letter
		# print bin(frame), "frame"
	# print "Pattern is in array:", found

wrapped = wrapper(move_frame, pattern1, nucleotides, len(pattern1))
times = timeit.timeit(wrapped, number=100)
print times, "3 letter pattern"
wrapped = wrapper(move_frame, pattern2, nucleotides, len(pattern2))
times = timeit.timeit(wrapped, number=100)
print times, "6 letter pattern"
wrapped = wrapper(move_frame, pattern3, nucleotides, len(pattern3))
times = timeit.timeit(wrapped, number=100)
print times, "9 letter pattern"
wrapped = wrapper(move_frame, pattern4, nucleotides, len(pattern4))
times = timeit.timeit(wrapped, number=100)
print times, "20 letter pattern"

# print bin(str_to_num(pattern))
# move_frame(pattern, nucleotides)