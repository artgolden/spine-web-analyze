# -*- coding: utf-8 -*-
import sys
import math

if len(sys.argv) < 2:
	r = int(input("Введите r:"))
else:
	r = int(sys.argv[1])
sqA = round(math.sqrt(r))
if sqA ** 2 > r:
	a = sqA - 1
else:
	a = sqA
rem = r - a ** 2
#print("rem=", rem)
sqB = round(math.sqrt(rem))
if sqB ** 2 + a ** 2 > r:
	b = sqB - 1
else:
	b = sqB

print("a=", a, "a^2=", a ** 2)
print("b=", b, "b^2=", b ** 2)
print("\na^2 + b^2 = ", a ** 2 + b ** 2)
