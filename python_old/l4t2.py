a = [int(x) for x in input().split()]
#
# a = eval(input())
#

# для всех x, т.ч. 0 <= x < i, верно:
#a0[x] = a[len(a0) - x - 1], a0[len(a0) - x - 1] = a[x]
for i in range(0, len(a) // 2):
	a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
print(a)