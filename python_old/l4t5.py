array = [int(x) for x in input('array: ').split()]
a = int(input('a: '))
l = 0
r = len(array) - 1
sw = True
while l <= r:
	middle_index = (l + r) // 2
	middle_value = array[middle_index]
	if a > middle_value:
		l = middle_index + 1
	elif a < middle_value:
		r = middle_index - 1
	else:
		print('a exists in array')
		sw = False
		break
if sw:
	print('a does not exist in array')

#test: '0
#0' 'array: a: a exists in array'
#test: '0
#1' 'array: a: a does not exist in array'
#test: '0 1
#1' 'array: a: a exists in array'
#test: '1 2 3 5 6 8 9
#9' 'array: a: a exists in array'