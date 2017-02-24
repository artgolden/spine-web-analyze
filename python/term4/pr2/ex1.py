
import Tkinter
import random
canvas_size = 500

x = 250
y = 250
delay = 10
timer = 0
color = 0
clr = ["red", "green", "blue", "white"]

def step():
  	global x, y, timer, color
  	if timer == 1000:
  		if color != 3:
  			color += 1
  		else:
  			color = 0
  		timer = 0
  	else:
  		timer += 1
	x += random.randint(-1, 1)
	y += random.randint(-1, 1)
	canvas.create_line([x, y], [x + 1, y], fill=clr[color])
	root.after(delay, step)

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='black')
canvas.pack()
step()

root.mainloop()