from __future__ import division
from numpy import sqrt,power
import Tkinter

def sign(x):
	if x >= 0:
		return 1
	else: 
		return -1

def hopalong(x0,y0,n,a=-55,b=-1,c=-42):
 def update(x,y):
  x1 = y-sign(x)*sqrt(abs(b*x+c))
  y1 = a-x
  return x1,y1
 xx = []
 yy = []
 for _ in xrange(n):
  x0,y0 = update(x0,y0) 
  xx.append(x0)
  yy.append(y0)
 return xx,yy



canvas_size = 1000
mg = 200
of = 600
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='black')
canvas.pack()
xx, yy = hopalong(1,1,100000, 0.4, 1, 0)
for i in range(len(xx)):
 canvas.create_line([of + xx[i] * mg, of + yy[i] * mg], [of + xx[i] * mg, of + yy[i] * mg], fill='white')




root.mainloop()