

class Node:
<<<<<<< HEAD
	def __init__(self, name):
		self.name = name
		self.children = []
		self.color = "white"
		self.paths = []
=======
    def __init__(self, name):
        self.name = name
        self.children = []
        # self.parents = []
        self.color = "white"
        self.paths = []
>>>>>>> 426d272dfb6c61356a4ecc5effec1bfae4179cfb

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

<<<<<<< HEAD
	if parent in nodes.keys():
		parent = nodes[parent] # Put Node object with name "parent" in parent
		if child in nodes.keys():
			child = nodes[child]
			parent.children.append(child)
		else:
			nodes[child] = Node(child) # added new Node object to dictionary 
			child = nodes[child]
			parent.children.append(child)
	else:
		nodes[parent] = Node(parent)
		parent = nodes[parent] # Put Node object with name "parent" in parent
		if child in nodes.keys():
			child = nodes[child]
			parent.children.append(child)
		else:
			nodes[child] = Node(child) # added new Node object to dictionary 
			child = nodes[child]
			parent.children.append(child)
	return nodes

def print_graph(nodes):
	for i in nodes.values():
		print i.name
		t = ""
		print i.paths
		for j in i.children:
			t += j.name
		print "children----", t
	print "==========="

def wide_search(nodes, start, end):
	if start not in nodes.keys() and end not in nodes.keys():
		print "start or end does not exist in nodes"
		quit(1)
	start = nodes[start]
	end = nodes[end]
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
						print "Path: ", i.paths[0] + j.name # Corrected 
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
wide_search(nodes, "c", "f")
# print_graph(nodes)
=======
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
        tmp = ""
        if len(i.paths):
            print i.paths
        for j in i.children:
            tmp += j.name
        print "children----", tmp
        tmp = ""
    print "==========="
>>>>>>> 426d272dfb6c61356a4ecc5effec1bfae4179cfb

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
                        # print i.paths, "hhhhhhhhhhh"
                        print "Path: ", i.paths[0] + j.name
                        found = True
                    for k in i.paths:
                        j.paths.append(k + j.name)
                    new_queue.append(j)
                    j.color = "grey"
        queue = new_queue        

NODES = create_dict("graph2.txt")
wide_search(NODES, "e", "j")
print_graph(NODES)
