import random
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def merge_sorted(theList1,theList2):
    sortedList = []
    counter1 = 0
    counter2 = 0

    while True:
        if counter1 == len(theList1):
            return sortedList + theList2[counter2:]

        if counter2 == len(theList2):
            return sortedList + theList1[counter1:]

        if theList1[counter1] < theList2[counter2]:
            sortedList.append(theList1[counter1])
            counter1 += 1
        else:
            sortedList.append(theList2[counter2])
            counter2 += 1

def merge_sort_iterative(theList):

    theNewList = map(lambda x: [x], theList)
    theLength = 1

    while theLength < len(theList):
        theNewNewList = []

        pairs = zip(theNewList[::2], theNewList[1::2])

        for pair in pairs:
            theNewNewList.append( merge_sorted( pair[0], pair[1] ) )

        if len(pairs) * 2 < len(theNewList):
            theNewNewList.append(theNewList[-1])

        theLength *= 2
        theNewList = theNewNewList

    return theNewNewList[0]

def correct_created_inverses(j, array):
	while array[j - 1] > array[j]:
		array[j], array[j - 1] = array[j - 1], array[j]
		if j > 1:
			j -= 1
		else: 
			break
	return array

def bubble_sort(array):

	invert = True
	inner_cycles = 0
	while invert == True:
		invert = False
		for j in range(len(array) - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				invert = True
				array = correct_created_inverses(j, array)
				inner_cycles += 1
	# print "bubble sorted:"
	# print array, inner_cycles
	return array


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot - 1)
        quicksort(myList, pivot + 1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap places
            myList[left], myList[right] = myList[right], myList[left]
    # swap start with myList[right]
    myList[start], myList[right] = myList[right], myList[start]
    return right

def sort(array):
	array.sort()
	return array

def compare_sorted(array):
	bubble = bubble_sort(array)
	quick = quicksort(array, 0, len(array) - 1)
	merge = merge_sort_iterative(array)
	if bubble == quick == merge:
		print "All lists sorted identicaly."
	else:
		print "Not identical sorting."
# arr = [int(x) for x in '4 7 3 5 8 2 3 6 8 9'.split(' ')]
# arr = [int(x) for x in range(100) ]
arr = random.sample(xrange(200), 200)
a = 1

wrapped = wrapper(quicksort, arr, 0, len(arr) - 1)
times = timeit.timeit(wrapped, number=100)
print times, "quicksort"
wrapped = wrapper(bubble_sort, arr)
times = timeit.timeit(wrapped, number=100)
print times, "bubble"
wrapped = wrapper(merge_sort_iterative, arr)
times = timeit.timeit(wrapped, number=100)
print times, "merge_sort_iterative"
wrapped = wrapper(sort, arr)
times = timeit.timeit(wrapped, number=100)
print times, "native"

compare_sorted(arr)
# bubble = bubble_sort(arr)

# quick = quicksort(arr, 0, len(arr) - 1)
# st = "quick: "
# for i in quick:
# 	st += str(i) + ' '
# print st

# st = "bubble: "
# for i in bubble:
# 	st += str(i) + ' '
# print st