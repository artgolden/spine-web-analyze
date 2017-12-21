from weight_queue import QueueWithWeight

class Node:
    def __init__(self, name):
        self.name = name
        self.weight = float('inf')
        self.color = "white"
        self.children = {}
        self.paths = []


class Graph:
    def __init__(self, file_name=None):
        self.nodes = {}
        self.que = QueueWithWeight()
        if file_name:
            self.create_graph(file_name)

    def create_graph(self, file_name):        
        data = open(file_name, "r")
        for line in data:
            self.process_string(line)
        data.close()



    def process_string(self, string):
        ar = string.strip().split(" ")
        parent = ar[0]
        child = ar[1]
        weight = int(ar[2])

        parent = self.add_Node_if_missing(parent)
        child = self.add_Node_if_missing(child)
        parent.children[child] = weight

    def add_Node_if_missing(self, elem):
        if not elem in self.nodes.keys():
            self.nodes[elem] = Node(elem)
        return self.nodes[elem]


    def print_graph(self):
        for i in self.nodes.values():
            print i.name
            print "Weight ", i.weight
            if i.children:
                for j in i.children.keys():
                    if j:
                        print "children----" + j.name + str(i.children[j])
        print "==========="
        
    
    def deikstra_search(self, start):
        if start not in self.nodes.keys():
            print "start does not exist in self.nodes"
            quit(1)
        start = self.nodes[start]
        start.paths = [start.name]
        start.color = "grey"
        start.weight = 0
        self.que.add(start)
        while self.que.queue_dict:
            parent = self.que.pop()
            parent.color = "black"
            if parent.children:
                for child in parent.children.keys():
                    self.relax_and_add_to_queue(parent, child)

    def relax_and_add_to_queue(self, parent, child):
        if child.color != "black":
            self.relaxation(parent, child)
            if child.color == "white":
                self.que.add(child)
                child.color = "grey"
        
    def relaxation(self, pre, nex):
        old_weight = nex.weight
        if nex.weight > (pre.weight + pre.children[nex]):
            nex.weight = pre.weight + pre.children[nex]
            if old_weight != float('inf'):
                if nex in self.que.queue_dict[old_weight]:
                    self.que.change(nex, old_weight)

graph = Graph("/home/tema/dev/Algoritms/graph_dei2.txt")
graph.deikstra_search("s")
graph.print_graph()
