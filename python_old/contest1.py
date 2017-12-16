
def find_gcd(array):
	for i in range(len(array) - 1):
		a = array[i]
		b = array[i + 1]
		while a > 0:
			a, b = max(a, b), min(a, b)
			a %= b
		array[i + 1] = max(a, b)
	return array[len(array) - 1]


n = int(input())
array = []
for i in range(n):
	array.append(int(input()))
print(find_gcd(array))
#print(find_gcd([1,2,3]))
#print(find_gcd([129846,2]))
#print(find_gcd([333,99,123]))
#print(find_gcd([4,2]))


