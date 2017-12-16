# -*- coding: utf-8 -*-
import sys
import math

if len(sys.argv) < 2:
	r = int(input("Введите r:"))
else:
	r = int(sys.argv[1])

def digory(A, B):
	return A ** 2 + B ** 2

a = 0
b = 0
while r < digory(a, b):
	a += 1
	while r < digory(a, b):
		b += 1
print("a =", a, "b =", b, "")