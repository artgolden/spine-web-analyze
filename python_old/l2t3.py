'''Finding lcm(a,b) with two methods'''
import sys
def gcd(a, b):
	while a > 0:
		a, b = max(a, b), min(a, b)
		a %= b
	return max(a, b)

if len(sys.argv) != 4:
	print("Error: Wrong number of arguments\nUsage: python3 l2t3.py a b switch[a,b]")
	exit(1)
a, b = int(sys.argv[1]), int(sys.argv[2])
switch = str(sys.argv[3])

if switch == 'a':
	i = 1
	while i <= a * b:
		if i % a == 0 and i % b == 0:
			print("lcm(a,b) =", i)
			break
		i += 1
elif switch == 'b':
	print("lcm(a,b) =", abs(a * b) // gcd(a, b))
else:
	print("Error: Wrong arguments\n Usage: python3 l2t3.py a b switch[a,b]")
