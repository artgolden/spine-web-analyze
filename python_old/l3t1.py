'''n**2**k in O(k) iterations'''
a = int(input('a:'))
k = int(input('k:'))
print ('a^2^k =', a**(2**k))
for i in range(k):
	a *= a
print ('a**2**k =', a)
