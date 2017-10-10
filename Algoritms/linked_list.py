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

	def sort(self):
		def correct_created_inverses(self, curr):
			if curr.next != None:
				while curr.data > curr.next.data:
					curr.data, curr.next.data = curr.next.data, curr.data
					if curr.next == None:
						curr = curr.next
					else:
						break
			else: pass

		invert = True
		while invert == True:
			invert = False
			curr = self.tail
			while curr.prev != None:
				if curr.data < curr.prev.data:
					curr.data, curr.prev.data = curr.prev.data, curr.data
					invert = True
					correct_created_inverses(self, curr)
				else:
					curr = curr.prev
	def invert(self):
		start = self.root
		end = self.tail
		if self.len > 1:
			while start.next != end and start.next != end.prev:
				start.data, end.data = end.data, start.data
				start = start.next
				end = end.prev
			start.data, end.data = end.data, start.data

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
d.append(7)
d.append(3)
d.append(6)
d.append(5)
d.append(9)
d.append(10)
d.append(4)

d.show()
d.sort()
d.show()
d.invert()
d.show()




		