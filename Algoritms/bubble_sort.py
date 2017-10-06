
def correct_created_inverses(j, array):
	while array[j - 1] < array[j]:
		array[j], array[j - 1] = array[j - 1], array[j]
		if j > 1:
			j -= 1
		else: 
			break



array = [int(x) for x in '4 7 3 5 8 2 3 6 8 9'.split(' ')]
a = 1

invert = True
inner_cycles = 0
while invert == True:
	invert = False
	for j in range(len(array) - 1):
		if array[j] < array[j + 1]:
			array[j], array[j + 1] = array[j + 1], array[j]
			invert = True
			correct_created_inverses(j, array)
			inner_cycles += 1
print array, inner_cycles
	
