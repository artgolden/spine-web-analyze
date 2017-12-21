class Node:
    def __init__(self, name):
        self.name = name
        self.weight = float('inf')
        self.children = {}


class Graph:
    def __init__(self, file_name=None):
        self.nodes = {}
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

        if parent in self.nodes.keys():
            parent = self.nodes[parent] # Put Node object with name "parent" in parent
            if child in self.nodes.keys():
                child = self.nodes[child]
                parent.children[child] = weight
            else:
                self.nodes[child] = Node(child) # added new Node object to dictionary 
                child = self.nodes[child]
                parent.children[child] = weight
        else:
            self.nodes[parent] = Node(parent)
            parent = self.nodes[parent] # Put Node object with name "parent" in parent
            if child in self.nodes.keys():
                child = self.nodes[child]
                parent.children[child] = weight
            else:
                self.nodes[child] = Node(child) # added new Node object to dictionary 
                child = self.nodes[child]
                parent.children[child] = weight

    def print_graph(self):
        for i in self.nodes.values():
            print i.name
            print "Weight ", i.weight
            if i.children:
                for j in i.children.keys():
                    if j:
                        print "children----" + j.name + str(i.children[j])
        print "==========="
       
    def relaxation(self, pre, nex):
        if nex.weight > (pre.weight + pre.children[nex]):
            nex.weight = pre.weight + pre.children[nex]
            # print pre.name, pre.weight,  "======"
            # print nex.name, nex.weight
            return True
        return False
    
    def bellman_search(self, start):
        start = self.nodes[start]
        start.weight = 0
        changed = True
        count = 0
        # while changed and count < len(self.nodes.keys()):
        while changed:
            changed = False
            for i in self.nodes.values():
                for j in i.children:
                    # print j.name
                    ch = self.relaxation(i, j)
                    changed = changed or ch
                # print "----"
            count += 1
        print count

graph = Graph("/home/tema/dev/Algoritms/graph_dei2.txt")
graph.bellman_search("s")
graph.print_graph()
    