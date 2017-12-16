<<<<<<< HEAD
import sys
if len(sys.argv) != 2:
	print('Wrong number of arguments.\nUsage: l4t0.py -(a,b)')

size = int(input())
if size <= 0:
	print('Empty array.')
	exit()
a = []
for i in range(size):
	a.append(int(input()))

if sys.argv[1] == '-a':
	maxx = a[0]
	for i in range(size):
		if a[i] > maxx:
			maxx = a[i]
	print('greatest number =', maxx)
elif sys.argv[1] == '-b':
	max1 = a[0]
	max2 = a[0]
	for i in range(size):
		if a[i] >  max1:
			max2 = max1
			max1 = a[i]
=======
import sys
if len(sys.argv) != 2:
	print('Wrong number of arguments.\nUsage: l4t0.py -(a,b)')

size = int(input())
if size <= 0:
	print('Empty array.')
	exit()
a = []
for i in range(size):
	a.append(int(input()))

if sys.argv[1] == '-a':
	maxx = a[0]
	for i in range(size):
		if a[i] > maxx:
			maxx = a[i]
	print('greatest number =', maxx)
elif sys.argv[1] == '-b':
	max1 = a[0]
	max2 = a[0]
	for i in range(size):
		if a[i] >  max1:
			max2 = max1
			max1 = a[i]
>>>>>>> 426d272dfb6c61356a4ecc5effec1bfae4179cfb
	print('first greatest number =', max1 ,'second greatest number =', max2)