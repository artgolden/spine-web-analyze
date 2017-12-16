#def who_is_more(ar1p, ar2p, m):


def find_matching(array1, array2):
	amount = 0
#	if len(array1) < len(array2):
#		array1 , array2 = array2, array1
	ar1p = 0
|	for i in range(len(array2) - 1 + len(array1) - 1 + 1):
		print(ar1p, ar2p, i, amount)
		if ar1p > len(array1) - 1 or ar2p > len(array2) - 1:
			break
		if array1[ar1p] < array2[ar2p]:
			ar1p += 1
#			print('array1[ar1p] < array2[ar2p]')
		elif array1[ar1p] > array2[ar2p]:
			ar2p += 1
#			print('array1[ar1p] > array2[ar2p]')
		else:
			amount += 1
			ar1p += 1
			ar2p += 1
	return amount
print(find_matching([1], [1]))
