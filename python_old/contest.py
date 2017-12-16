
def find_gcd(array):
	if len(array) == 1:
		print(array[0])
	l = []
	lit = 0
	it = 0
	while it <= len(array) - 2:
		a = array[it]
		b = array[it + 1]
		while a > 0:
			a, b = max(a, b), min(a, b)
			a %= b
		lit += 1
		l.append(max(a, b))
		it += 2
	find_gcd(l)

n = int(input())
array = []
for i in range(n):
	array.append(int(input()))
find_gcd(array)