import random
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
	print "bubble sorted:"
	print array, inner_cycles
	return array

# def quick_sort(A, fr, to):
# 	if fr < to:
# 		q = partition(A, fr, to)
# 		quick_sort(A, fr, q - 1)
# 		quick_sort(A, q + 1, to)


# def partition(a, fr, to):
# 	q = a[fr]
# 	i, i1, i2 = fr, fr, to - 1
# 	while i1 != i2:
# 		while a[i2] >= q:
# 			i2 -= 1
# 		a[i], a[i2] = a[i2], a[i]
# 		a[i2], q = q, a[i2]
# 		i = i2
# 		while a[i1] < q:
# 			i += 1
# 			a[i], a[i1] = a[i1], a[i]
# 			a[i1], q = q, a[i1]
# 			i = i1
# 	return i

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
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
    # swap start with myList[right]
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    return right



# arr = [int(x) for x in '4 7 3 5 8 2 3 6 8 9'.split(' ')]
arr = [int(x) for x in range(100) ]
a = 1

bubble = bubble_sort(arr)
quick = quicksort(arr, 0, len(arr) - 1)
print quick