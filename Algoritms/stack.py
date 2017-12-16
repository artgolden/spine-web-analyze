class Stack:
	def __init__(self):
		self.array = []
		self.len = 0

	def push(self, elem):
		self.array.append(elem)
		self.len += 1

	def pop(self):
		if self.len != 0:
			self.len -= 1
			return self.array.pop()

	def sprint(self):
		print self.array

	def get(self):
		return self.array
