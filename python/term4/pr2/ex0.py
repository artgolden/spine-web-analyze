
import Tkinter
import random
canvas_size = 500

x = 250
y = 250
delay = 10

def step():
  global x, y
  x += random.randint(-1, 1)
  y += random.randint(-1, 1)
  canvas.create_line([x, y], [x + 1, y], fill='white')
  root.after(delay, step)

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='black')
canvas.pack()
step()

root.mainloop()