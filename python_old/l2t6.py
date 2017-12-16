'''Printing k decimal places of the number 1/n'''
import sys
if len(sys.argv) != 3:
	print("Error: Wrong number of arguments\nUsage: python3 l2t6.py n k")
	exit(1)
n, k = int(sys.argv[1]), int(sys.argv[2])
kn = 10 ** k // n
fkn = 1 / n
out = ''
i = k
while kn < 10 ** i:
	out += '0'
	i -= 1
out = out[1:len(out)]

out += str(kn)

while len(out) > k:
	out = out[0:len(out) - 1]
	
print("k decimal places of the number k/n:", out, "\nk mod 1 / n =", fkn)