import random
import math
import Tkinter
canvas_size = 500

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
  mg = 100
  of = 200
  canvas.create_line([of + x * mg, of + y * mg], [of + 1 + x * mg, of + y * mg], fill='white')
  xn = x
  x = (y - sign(x)*math.sqrt(abs(b * x - c))) 
  y = (a - xn)
  n += 1
  if n < 20000:
    root.after("idle", step)
  	#root.after(1, step)

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='black')
canvas.pack()
step()

root.mainloop()