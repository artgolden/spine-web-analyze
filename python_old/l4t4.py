n = input('Введите n:')

def extend_list(l, n):
	for c in range(n + 1 - len(l)):
		res.append(0)
	l[n] = 1

def add(l, n):
	if n > len(l) - 1:
		extend_list(l, n)
	else:
		l[n] += 1

res = []
for i in range(len(n)):
	add(res, int(n[i]))	
for i in range(len(res)):
	if res[i] != 0:
		print(res[i], end = '')
		print(i, end = '')
print('')