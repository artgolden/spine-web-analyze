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

        parent = self.add_Node_if_missing(parent)
        child = self.add_Node_if_missing(child)
        parent.children[child] = weight

        
    def add_Node_if_missing(self, elem):
        if not elem in self.nodes.keys():
            self.nodes[elem] = Node(elem)
        return self.nodes[elem]

    def print_graph(self):
        for i in self.nodes.values():
            print "Node: " + i.name
            print "Weight ", i.weight
            if i.children:
                children = ""
                for j in i.children.keys():
                    if j:
                        children += j.name + "-" + str(i.children[j]) + ", "
                print "Child-distance: " + children
            print ""
        print "==========="

    def relaxation(self, pre, nex):
        if nex.weight > (pre.weight + pre.children[nex]):
            nex.weight = pre.weight + pre.children[nex]
            return True
        return False
    
    def bellman_search(self, start):
        start = self.nodes[start]
        start.weight = 0
        changed = True
        count = 0
        while changed and count < len(self.nodes.keys()):
            changed = False
            for parent in self.nodes.values():
                for child in parent.children:
                    relax_occured = self.relaxation(parent, child)
                    changed = changed or relax_occured
            count += 1

graph = Graph("/home/tema/dev/Algoritms/graph_dei2.txt")
graph.bellman_search("s")
graph.print_graph()
    
