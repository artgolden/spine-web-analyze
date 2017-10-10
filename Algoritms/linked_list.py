class Node(object):
	"""docstring for Node"""
	def __init__(self, data, prev, next ):
		self.data = data
		self.prev = prev
		self.next = next
		

class DoubleLinkedList(object):
	"""docstring for DoubleLinkedList"""
	def __init__(self):
		self.len = 0
		self.root = None
		self.tail = None

	def append(self, data):
		new_node = Node(data, None, None)
		if self.root == None:
			self.root = self.tail = new_node
			self.len += 1
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
			self.len += 1

	def remove(self, data):
		if self.root != None:
			curr = self.tail
			st = ""
			while True:
				if curr.data == data:
					if curr.prev == None:
						curr.next.prev = None
						self.root = curr.next 
						print "Found beginning"
						break
					if curr.next == None:
						self.tail = curr.prev
						curr.prev.next = None
						print "Found end"
						break
					if self.tail != curr and self.root != curr:
						curr.next.prev, curr.prev.next = curr.prev, curr.next
						print "Found inside"
						break
				else: pass
				print curr.data
				if curr.prev != None:
					curr = curr.prev
				else: break

		else:
			print "List is empty"

	def show(self):
		if self.root != None:
			curr = self.tail
			st = ""
			while curr.prev != None:
				st += str(curr.data) + " "
				curr = curr.prev
			print st + str(curr.data)
			print "*"*50
		else:
			print "List is empty"


d = DoubleLinkedList()
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.show()
d.remove(3)
d.show()




		