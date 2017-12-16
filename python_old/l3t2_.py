'''a**n for O( log(n) ) iterations'''
a = int(input('a:'))
n = int(input('n:'))
print('a^n =', a ** n)
mask = 1
digit = 0
while mask <= n:
	mask *= 2
	digit += 1
mask //= 2
print('mask =', mask)
digit -= 1
print('digit =', digit)
res = 1
b = 1
while mask >= 1:
	if n // mask:
		b = a
		for i in range(digit):
			b *= b
		n = n - mask
		res *= b
	mask //= 2
	digit -= 1
print('a**n =', res)	