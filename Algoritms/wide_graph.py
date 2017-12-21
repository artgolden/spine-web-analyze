

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
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
    parent = add_Node_if_missing(parent, nodes_dict)
    child = add_Node_if_missing(child, nodes_dict)
    parent.children.append(child)
    return nodes_dict

def add_Node_if_missing(elem, nodes_dict):
    if not elem in nodes_dict.keys():
        nodes_dict[elem] = Node(elem)
    return nodes_dict[elem]

def print_graph(nodes_dict):
    for i in nodes_dict.values():
        print i.name
        tmp = ""
        if i.paths:
            print i.paths
        for j in i.children:
            tmp += j.name
        print "children----", tmp
        tmp = ""
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
    found = False
    while not found:
        new_queue = []
        for i in queue:
            for j in i.children:
                if j.color == "white":
                    if j == end:
                        print "Path: ", i.paths[0] + j.name
                        found = True
                    for k in i.paths:
                        j.paths.append(k + j.name)
                    new_queue.append(j)
                    j.color = "grey"
        queue = new_queue        


NODES = create_dict("/home/tema/dev/Algoritms/graph2.txt")
wide_search(NODES, "e", "j")
print_graph(NODES)
