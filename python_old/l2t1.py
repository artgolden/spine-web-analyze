'''Finding gcd(a,b) with three methods'''
import sys

if len(sys.argv) != 4:
	print("Error: Wrong number of arguments\nUsage: python3 l2t1.py a b switch[a,b,c]")
	exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])
switch = str(sys.argv[3])

if switch == 'a': # Search method
	div = min(a,b)
	while a % div != 0 or b % div != 0:
		div -= 1
	print("Greatest Common Divisor = ", div)
elif switch == 'b': # gcd(a - b, b) = gcd(a, b) method
	while a > 0:
		a, b = max(a, b), min(a, b)
		if a % b == 0:
			break
	print("Greatest Common Divisor = ", b)
elif switch == 'c': # gcd(a mod b, b) = gcd(a, b) method
	while a > 0:
		a, b = max(a, b), min(a, b)
		a %= b
	print("Greatest Common Divisor = ", max(a, b))
else:
	print("Error: Wrong arguments\n Usage: python3 l2t1.py a b switch[1,2,3]")

