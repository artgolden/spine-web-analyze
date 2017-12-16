'''a**n for O( log(n) ) iterations'''
a = int(input('a:'))
n = int(input('n:'))
print('a^n =', a ** n)
res = 1
while n > 0:
	if n % 2:
		res *= a
	a *= a
	n //= 2
print('a**n =', res)		