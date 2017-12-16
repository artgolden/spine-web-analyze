'''Checking if n is a prime number'''
import sys
if len(sys.argv) != 2:
	print("Error: Wrong number of arguments\nUsage: python3 l2t3.py n")
	exit(1)
n = int(sys.argv[1])
i = 2
while i * i <= n:
	if n % i == 0:
		print("n is NOT a prime number")
		exit()
	i += 1
print("n is a prime number")