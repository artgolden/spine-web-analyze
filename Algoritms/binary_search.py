# array = [int(x) for x in input('array: ').split(' ')]
# arr = input('array: ')
# array = []
# for i in arr:
# 	array.append(int(i))
# a = int(input('a: '))

array = [int(x) for x in '1 2 6 7'.split(' ')]
a = 1

def binary_search(array,a):
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
			# print middle_index
			print('a exists in array')
			sw = False
			break
	if sw:
		print('a does not exist in array')

binary_search(array, a)
