'''Finding x, y such that xa + yb = gcd(a,b)'''
import sys

def gcd(a, b):
	while a > 0:
		a, b = max(a, b), min(a, b)
		print('a=', a, 'b=', b, '\na//b=', a // b, '\n(a)mod(b)=', a % b)
		a %= b
	return max(a, b)

###########################################################################

if len(sys.argv) != 4:
	print("Error: Wrong number of arguments\nUsage: python3 l2t2.py a b switch[a,b]")
	exit(1)

a , b = int(sys.argv[1]), int(sys.argv[2])
switch = str(sys.argv[3])
d = gcd(a, b)
if switch == 'a':
	x, y = a, b
	while x >= -a:
		y = b
		while y >= -b:
			if x * a + y * b == d:
				print("x =", x, "y =", y,"xa + yb=", x*a+y*b, "gcd(a,b) =", d)
				exit()
			y -= 1
		x -= 1
	print("gcd =", d)
	print("No x, y fitting conditions")
elif switch == 'b':
	x = 1
	while x < b :
		if (d - x*a) % b == 0 or (-d - x * a) % b == 0:
			y = (d - x * a) // b
			if (-d - x * a) % b == 0:
				x,y = -x, -y
			print("x =", x, "y =", y, "xa + yb=", x * a + y * b, "gcd(a,b) =", d)
			exit()
		x += 1
	print("gcd =", d)
	print("No x, y fitting conditions")
elif switch == 'c':
	print('NOT done')
else:
	print("Error: Wrong number of arguments\nUsage: python3 l2t2.py a b switch[a,b]")