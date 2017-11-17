'''Searching substring in string of nucleotides'''
import timeit
nucleotides = 'AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGAGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAATGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCTGGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGAGGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAGATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGACGCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCAGTGTGGGTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGCGACCTAGGGCTGGCGGGCAGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGCTCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC'
nucleotides1 = 'AGCCCTCCAGGGACAGGCTGCATC'
nucleotides2 = 'AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGAGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACTGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGT'
pattern1 = 'GGG'
pattern2 = 'GGGTCTGGGTCT'
pattern3 = 'GGGGTTCATGGGGGTTCATGGGGGTTCATG'
pattern4 = 'GGGGTTCATGTGACTCAGTAGGGGTTCATGTGACTCAGTA'




def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def letter_to_dec(letter):
	b = 5
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
	n = letter_to_dec(line[len(line) - 1])
	for i in range(len(line) - 2, -1, -1):
		n *= 10
		n += letter_to_dec(line[i])
	return n

def compare_numbers(matrix, frame, mismatch):
	if matrix == frame:
		return True
	else:
		return False

def move_frame(pattern, nucleotides, length, mismatch):
	matrix = str_to_num(pattern)
	frame = str_to_num(nucleotides[:length])
	found = False
	print frame, "frame", nucleotides[:length]
	for i in range(length, len(nucleotides) - length):
		if compare_numbers(matrix, frame, mismatch):
			found = True
			print "Pattern is in array:", found
			quit(0)
		frame -= frame % 10
		frame /= 10
		print frame, "frame"
		letter = letter_to_dec(nucleotides[i])
		print frame, "frame", nucleotides[i]
		frame += letter * 10 ** (length - 1)
		print frame, "frame"
	print "Pattern is in array:", found

# wrapped = wrapper(move_frame, pattern1, nucleotides, len(pattern1))
# times = timeit.timeit(wrapped, number=100)
# print times, "3 letter pattern"
# wrapped = wrapper(move_frame, pattern2, nucleotides, len(pattern2))
# times = timeit.timeit(wrapped, number=100)
# print times, "6 letter pattern"
# wrapped = wrapper(move_frame, pattern3, nucleotides, len(pattern3))
# times = timeit.timeit(wrapped, number=100)
# print times, "9 letter pattern"
# wrapped = wrapper(move_frame, pattern4, nucleotides, len(pattern4))
# times = timeit.timeit(wrapped, number=100)
# print times, "20 letter pattern"

# print "======================================================="

# wrapped = wrapper(move_frame, pattern1, nucleotides2, len(pattern1))
# times = timeit.timeit(wrapped, number=100)
# print times, "3 letter pattern"
# wrapped = wrapper(move_frame, pattern2, nucleotides2, len(pattern2))
# times = timeit.timeit(wrapped, number=100)
# print times, "6 letter pattern"
# wrapped = wrapper(move_frame, pattern3, nucleotides2, len(pattern3))
# times = timeit.timeit(wrapped, number=100)
# print times, "9 letter pattern"
# wrapped = wrapper(move_frame, pattern4, nucleotides2, len(pattern4))
# times = timeit.timeit(wrapped, number=100)
# print times, "20 letter pattern"

# print bin(str_to_num(pattern))
move_frame(pattern1, nucleotides1, len(pattern1), 0)