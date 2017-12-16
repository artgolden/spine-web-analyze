a = [int(x) for x in input().split()]
#
# l = []
# for x in input().split()
#     l.append(int(x))
# return l
#
if len(a) == 0:
	print('Empty array')
	exit()
amount = 0

for i in range(0, len(a)):
	gr_l = True
	if i - 1 >= 0:
		if a[i] <= a[i - 1]:
			gr_l = False
	gr_r = True	
	if i + 1 < len(a):
		if a[i] <= a[i + 1]:
			gr_r = False
	if gr_l and gr_r:
		amount += 1
print('Number of elements =', amount)