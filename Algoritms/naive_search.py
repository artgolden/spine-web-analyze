

array = [int(x) for x in '1 2 6 7'.split(' ')]
a = 1

def naive_search(array, a):
	found = False
	for i in array:
		if i == a:
			found = True

	print "a exists in array:", found
naive_search(array, a)