

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

def process_string(string, nodes_dict):
    ar = string.strip().split(" ")
    parent = ar[0]
    child = ar[1]

    if parent in nodes_dict.keys():
        parent = nodes_dict[parent] # Put Node object with name "parent" in parent
        if child in nodes_dict.keys():
            child = nodes_dict[child]
            parent.children.append(child)
            # child.parents.append(parent)
        else:
            nodes_dict[child] = Node(child) # added new Node object to dictionary 
            child = nodes_dict[child]
            parent.children.append(child)
            # child.parents.append(parent)
    else:
        nodes_dict[parent] = Node(parent)
        parent = nodes_dict[parent] # Put Node object with name "parent" in parent
        if child in nodes_dict.keys():
            child = nodes_dict[child]
            parent.children.append(child)
            # child.parents.append(parent)
        else:
            nodes_dict[child] = Node(child) # added new Node object to dictionary 
            child = nodes_dict[child]
            parent.children.append(child)
            # child.parents.append(parent)        
    return nodes_dict

def print_graph(nodes_dict):
    for i in nodes_dict.values():
        print i.name
        t = ""
        if len(i.paths): print i.paths
        for j in i.children:
            t += j.name
        print "children----", t
        t = ""
    print "==========="

def wide_search(nodes_dict, start, end):
    if start not in nodes_dict.keys() and end not in nodes_dict.keys():
        print "start or end does not exist in nodes_dict"
        quit(1)
    start = nodes_dict[start]
    end = nodes_dict[end]
    start.paths = [start.name]
    start.color = "grey"
    queue = [start]
    o = 0
    Found = False
    while not Found:
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


nodes = create_dict("graph2.txt")
wide_search(nodes, "e", "j")
print_graph(nodes)


