def find_one_missing(array):
	n = len(array)
	summ = 0
	for i in range(n):
		summ += array[i]
	missing = ((n + 0) * (n + 1) // 2) - summ
	return missing

def find_two_missing(array):
	n = len(array) + 2
	mis1 = 0
	mis2 = 0
	mist = [0 for c in range(n)]
	for i in range(n - 2):
		mist[array[i]] = 1
	sw = 1
	for a in range(n):
		if mist[a] == 0 and sw != 0:
			sw = 0
			mis1 = a
		if mist[a] == 0 and sw == 0:
			mis2 = a
	return mis1, mis2

import sys
array = [int(x) for x in input('array: ').split()]
if len(sys.argv) == 2:
	switch = sys.argv[1]
else:
	switch = '-a'

if switch == '-a':
	print(find_one_missing(array))
elif switch == '-b':
#	print(find_two_missing([0, 1, 3, 4, 7, 6, 10, 8, 9]))
	print(find_two_missing(array))
else:
	print('Wrong argument value, only ( -a, -b) are possible')
