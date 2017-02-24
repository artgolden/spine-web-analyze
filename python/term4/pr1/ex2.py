
arr = [ -1, -3, 1, -2, 5, -6, 7]

def sort_by_sign(array):
    i = True
    while i == True:
        i = False
        for j in range(len(array) - 1):
            if array[j] < 0 and array[j + 1] > 0:
                array[j], array[j + 1] = array[j + 1], array[j]
                i = True
    return array

print sort_by_sign(arr)