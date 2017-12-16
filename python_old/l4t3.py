a = [int(x) for x in input().split()]
prev = a[0]
print(a[0], end = ' ')
for i in range(1, len(a)):
	if prev != a[i]:
		print(a[i], end = ' ')
	prev = a[i]
print('')