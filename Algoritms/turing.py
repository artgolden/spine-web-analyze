class Turing(object):

	def __init__(self, initial_state=None, default_char='_'):
		self.program = {}
		self.state = initial_state
		self.tape = []
		self.position = 0
		self.default_char = default_char

	def rule(self, state, char, new_char, move, new_state):
		self.program[state, char] = new_char, move.upper(), new_state

	def step(self):
		new_char, move, new_state = self.program[self.state, self.tape[self.position]]
		self.tape[self.position] = new_char
		self.state = new_state
		if move in ("<", "L", "LEFT"):
			self.position -= 1
			while self.position < 0:
				self.tape.insert(0, self.default_char)
				self.position += 1
		elif move in (">", "R", "RIGHT"):
			self.position += 1
			while self.position >= len(self.tape):
				self.tape.append(self.default_char)
		elif move in (None, " ", "W", "WAIT"):
			pass
		elif move in ("!", "S", "STOP"):
			raise Stop()
		else:
			raise Exception("Illegal move:", move)

	def run(self, tape, position):
		self.tape = list(tape)
		self.position = position
		self.print_state()
		try:
			while True:
				self.print_state()
				self.step()
		except Stop:
			self.print_state()

	def print_state(self):
		print self.state, self.position, self.tape

	def validate(self, alphabet=None, states=None):
		if alphabet is not None:
			assert self.default_char in alphabet
		if states is not None:
			assert self.state in states
		for (state, char), (new_char, move, new_state) in self.program.items():
			if alphabet is not None:
				assert char in alphabet
				assert new_char in alphabet
			if states is not None:
				assert state in states
				assert new_state in states

class Stop(Exception):
	pass


import turing

tm = turing.Turing('q1', '0')
tm.rule('q0', '0', '0', 'S', 'q0')
tm.rule('q0', '1', '1', 'S', 'q1')
tm.rule('q1', '0', '1', '<', 'q0')
tm.rule('q1', '1', '0', '<', 'q1')
tm.validate('01', ('q0', 'q1'))
tm.run('11111', 4)