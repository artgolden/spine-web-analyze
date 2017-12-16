

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        # self.parents = []
        self.color = "white"
        self.paths = []

def create_dict(file_name):
    nodes = {}
    data = open(file_name, "r")

    for line in data:
        nodes = process_string(line, nodes)
    data.close()
    return nodes

def process_string(string, nodes):
    ar = string.strip().split(" ")
    parent = ar[0]
    child = ar[1]

    if parent in nodes.keys():
        parent = nodes[parent] # Put Node object with name "parent" in parent
        if child in nodes.keys():
            child = nodes[child]
            parent.children.append(child)
            # child.parents.append(parent)
        else:
            nodes[child] = Node(child) # added new Node object to dictionary 
            child = nodes[child]
            parent.children.append(child)
            # child.parents.append(parent)
    else:
        nodes[parent] = Node(parent)
        parent = nodes[parent] # Put Node object with name "parent" in parent
        if child in nodes.keys():
            child = nodes[child]
            parent.children.append(child)
            # child.parents.append(parent)
        else:
            nodes[child] = Node(child) # added new Node object to dictionary 
            child = nodes[child]
            parent.children.append(child)
            # child.parents.append(parent)        
    return nodes

def print_graph(nodes):
    for i in nodes.values():
        print i.name
        t = ""
        print i.paths
        for j in i.children:
            t += j.name
        print "children----", t
        t = ""
        # for j in i.parents:
        #     t += j.name
        # print "parents----", t
    print "==========="

def wide_search(nodes, start, end):
    start = nodes[start]
    end = nodes[end]
    start.paths = [start.name]
    start.color = "grey"
    queue = [start]
    o = 0
    found = False
    while not found:
        new_queue = []
        for i in queue:
            for j in i.children:
                if j.color == "white":
                    if j == end:
						# print i.paths, "hhhhhhhhhhh"
						print "Path: ", i.paths[0] + j.name
						Found = True
                    for k in i.paths:
                        j.paths.append(k + j.name)
                    new_queue.append(j)
                    j.color = "grey"
        queue = new_queue
        o += 1

        # new_queue = []
        # for i in queue:
        # queue = new_queue


nodes = create_dict("graph.txt")
wide_search(nodes, "A", "G")
print_graph(nodes)


