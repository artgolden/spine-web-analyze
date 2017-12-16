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
        self.nodes = {}
        data = open(file_name, "r")

        for line in data:
            self.nodes = self.process_string(line, self.nodes)
        data.close()
        return self.nodes

    def process_string(self, string, nodes_dict):
        ar = string.strip().split(" ")
        parent = ar[0]
        child = ar[1]
        weight = int(ar[2])

        if parent in nodes_dict.keys():
            parent = nodes_dict[parent] # Put Node object with name "parent" in parent
            if child in nodes_dict.keys():
                child = nodes_dict[child]
                parent.children[child] = weight
            else:
                nodes_dict[child] = Node(child) # added new Node object to dictionary 
                child = nodes_dict[child]
                parent.children[child] = weight
        else:
            nodes_dict[parent] = Node(parent)
            parent = nodes_dict[parent] # Put Node object with name "parent" in parent
            if child in nodes_dict.keys():
                child = nodes_dict[child]
                parent.children[child] = weight
            else:
                nodes_dict[child] = Node(child) # added new Node object to dictionary 
                child = nodes_dict[child]
                parent.children[child] = weight
        return nodes_dict

    def print_graph(self):
        # print self.nodes
        for i in self.nodes.values():
            print i.name
            print "Weight ", i.weight
            tmp = ""
            # if len(i.paths):
                # print i.paths
            if i.children:
                for j in i.children.keys():
                    if j:
                        # j = j[0]
                        # tmp += j.name
                        print "children----" + j.name + str(i.children[j])
            tmp = ""
        print "==========="
        
    def relaxation(self, pre, nex):
        # self.que.add()
        old_weight = nex.weight
        # print pre.weight, pre.children[nex]
        # quit(0)
        if nex.weight > (pre.weight + pre.children[nex]):
            nex.weight = pre.weight + pre.children[nex]
            if old_weight != float('inf'):
                if nex in self.que.queue_dict[old_weight]:
                    self.que.change(nex, old_weight)
    
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
            curr = self.que.pop()
            curr.color = "black"
            if curr.children:
                for i in curr.children.keys():
                    if i.color != "black":
                        self.relaxation(curr, i)
                        if i.color == "white":
                            self.que.add(i)
                            i.color = "grey"
        

# print node.weight
# que = QueueWithweight(node, node2)
# print que.queue_dict
graph = Graph("graph_dei2.txt")
graph.deikstra_search("s")
graph.print_graph()