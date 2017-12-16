class Queue:
	def __init__(self):
		self.array = []

	def put(self, elem):
		self.array.append(elem)

	def get(self):
		if len(self.array) != 0:
			return self.array.pop(0)
