# -*- coding: utf-8 -*-
import sys
import math

if len(sys.argv) < 2:
	r = int(input("Введите r:"))
else:
	r = int(sys.argv[1])

def degree(A, B):
	return A ** 2 + B ** 2

for a in range(r + 1):
	for b in range(r + 1):
		if degree(a, b) <= r:
			print(a, b, degree(a, b))
# print("a =", a, "b =", b, "\na^2 + b^2 = ", degree(a, b))