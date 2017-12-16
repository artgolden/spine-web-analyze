n = input('Введите n:')
NDIGITS = 10

def add(l, n):
	l[n] += 1

res = [0 for c in range(0,NDIGITS)]
for i in range(len(n)):
	add(res, int(n[i]))
for i in range(len(res)):
	if res[i] != 0:
		print(res[i], end = '')
		print(i, end = '')
print('')