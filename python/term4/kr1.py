
import Tkinter
import random

canvas_size = 500
# path = "C:/Users/PC/Fbb_work/Python_prog/FBB_work/python/term4/bow.jpg"
class Bow():
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.size = 50
        self.color = "blue"
        self.y_speed = 5
        self.parts = []
        self.draw()

    def draw(self):
        off = self.size
        x = self.x
        y = self.y
        self.parts.append(self.canvas.create_polygon([x + off // 2, y - off // 2], [x + off // 2, y + off // 2], [x, y], fill=self.color))
        self.parts.append(self.canvas.create_polygon([x - off // 2, y - off // 2], [x - off // 2, y + off // 2], [x, y], fill=self.color))
        # self.parts.append(self.canvas.create_polygon([x + off, y], [x + off, y + off], [x + off // 2, y + off // 2], fill=self.color))
    def move(self, x_speed):
        self.delete()
        self.y += self.y_speed
        self.x += x_speed
        border = canvas_size - self.size 
        if self.y > border:
            self.y -= border
        if self.x > border:
            self.x -= border
        self.draw()
    def delete(self):
        for i in self.parts:
            self.canvas.delete(i)
        self.parts = []

def step():
    for i in bows:
        i.move(random.randint(-5,5))
    root.after(100, step)
def on_click(event):
    # print 'u'
    # print "----", event.x, event.y
    for i in range(len(bows)):
        # print bows[i].x, bows[i].y
        if (abs(bows[i].x - event.x) <= 10) and (abs(bows[i].y - event.y)  <= 10):
            bows[i].delete()
            # print "deleteeee"

def on_move(event):
    pass


root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=canvas_size, height=canvas_size, background='white')
canvas.pack()
button = Tkinter.Button(root, text='move', width=30, command=step)
button.pack()

bows = []
for i in range(10):
    bows.append(Bow(canvas,\
     random.randint(50,450), random.randint(50,450)))
canvas.bind('<ButtonPress>', on_click)

root.mainloop()