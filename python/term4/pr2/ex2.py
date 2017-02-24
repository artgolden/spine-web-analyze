import random
import math
import Tkinter
canvas_size = 1000

x = 1
y = 1
delay = 1
n = 0

def sign(x):
	if x >= 0:
		return 1
	else: 
		return -1

def step():
  global x, y, n
  a, b, c = 0.4, 1, 0
  mg = 300
  of = 400
  canvas.create_line([of + x * mg, of + y * mg], [of + x * mg, of + y * mg], fill='white')
  xn = x
  x = (y - sign(x)*math.sqrt(abs(b * x - c))) 
  y = (a - xn)
  n += 1
  if n < 40000:
  	root.after("idle", step)

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='black')
canvas.pack()
step()

root.mainloop()