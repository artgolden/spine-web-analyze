'''Representing n as a product of primes'''
import sys
def prime_product(n):
	i = 1
	pr = ''
	while i <= n:
		i += 1
		if n % i == 0:
			pr += str(i) + ' '
			n = n // i
			i = 1
	return pr

if len(sys.argv) != 2:
	print("Error: Wrong number of arguments\nUsage: python3 l2t5.py n")
	exit(1)
n = int(sys.argv[1])

print("Product of primes: ", prime_product(n))