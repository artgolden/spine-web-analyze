import random

class Stack:
    def __init__(self, *argv):
        self.sta = []
        for a in argv:
            self.add(a)

    def add(self, elm):
        self.sta.append(elm)
        return self.sta

    def pop(self):
        return self.sta.pop(len(self.sta) - 1)

    def latest(self):
        return self.sta[len(self.sta) - 1]

    def leen(self):
        return len(self.sta)

class Queue:
    def __init__(self, *argv):
        self.que = []
        for a in argv:
            self.add(a)

    def add(self, elm):
        self.que.append(elm)
        return self.que

    def pop(self):
        return self.que.pop(0)

    def leen(self):
        return len(self.que)
                
class ver:
    def __init__(self, name = None, color = None, neigh = None):
        self.color = color
        self.neigh = neigh
        self.name = name
        
class graph:
    def __init__(self, vertex):
        self.vertex = dict()
        for a in vertex:
            #print (a)
            if a[0] not in self.vertex.keys():
                self.vertex[a[0]] = ver(name = a[0], color = "white", neigh = [a[1]])
            else:
                self.vertex[a[0]].neigh.append(a[1])
            self.vertex[a[1]] = ver(name = a[1], color = "white", neigh = [])

    def deep(self, start, stop):
        ver_now = self.vertex[start]
        stack = Stack(ver_now)
        write = []
        ver_now.color = "grey"
        while True:
            ver_now = [self.vertex[k] for k in ver_now.neigh if self.vertex[k].color == "white"]
            if len(ver_now) == 0:
                if stack.leen() == 0:
                    print ("Nor found")
                else:
                    la = stack.pop()
                    la.color = "black"
                    ver_now = stack.latest()
            else:
                ver_now = random.choice(ver_now)
                ver_now.color = "grey"
                stack.add(ver_now)
            if ver_now.name == stop:
                #write.append(ver_now.name)
                for i in range(stack.leen()):
                    k = stack.pop()
                    k.color = "black"
                    write.insert(0, k.name)
                break
        for i in write:
            print (i)
        return None

    def wide(self, start, stop):
        ver_now = self.vertex[start]

data = open("graph.txt", "r")
vertex = [line.strip().split() for line in data]
data.close()
#print (vertex)

start = "a"
stop = "g"
    
gr = graph(vertex)
gr.deep(start, stop)
            

    