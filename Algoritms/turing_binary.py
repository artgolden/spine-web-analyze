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

tm = turing.Turing('q0', '_')
tm.rule('q0', '=', '=', '>', 'q0')
tm.rule('q0', '1', '1', '>', 'q0')
tm.rule('q0', '0', '0', '>', 'q0')
tm.rule('q0', '+', '+', '>', 'q0')
tm.rule('q0', ';', ';', '<', 'det')

tm.rule('det', '_', '_', '<', 'det')
tm.rule('det', '0', '_', '<', 'fin_r0')
tm.rule('det', '1', '_', '<', 'fin_r1')
tm.rule('det', '+', '+', '<', 'g0')

tm.rule('fin_r0', '+', '+', '<', 'g0')
tm.rule('fin_r0', '0', '0', '<', 'fin_r0')
tm.rule('fin_r0', '1', '1', '<', 'fin_r0')

tm.rule('fin_r1', '+', '+', '<', 'g1')
tm.rule('fin_r1', '0', '0', '<', 'fin_r1')
tm.rule('fin_r1', '1', '1', '<', 'fin_r1')

tm.rule('g0', '1', '_', '<', 'fin_l1')
tm.rule('g0', '0', '_', '<', 'fin_l0')
tm.rule('g0', '_', '_', '<', 'g0')
tm.rule('g0', '=', '=', '<', 'Finito')

tm.rule('g1', '1', '_', '<', 'fin_l2')
tm.rule('g1', '0', '_', '<', 'fin_l1')
tm.rule('g1', '_', '_', '<', 'g1')

tm.rule('fin_l0', '=', '=', '<', 's0')
tm.rule('fin_l0', '0', '0', '<', 'fin_l0')
tm.rule('fin_l0', '1', '1', '<', 'fin_l0')

tm.rule('fin_l1', '=', '=', '<', 's1')
tm.rule('fin_l1', '0', '0', '<', 'fin_l1')
tm.rule('fin_l1', '1', '1', '<', 'fin_l1')

tm.rule('fin_l2', '=', '=', '<', 's2')
tm.rule('fin_l2', '0', '0', '<', 'fin_l2')
tm.rule('fin_l2', '1', '1', '<', 'fin_l2')

tm.rule('s0', '0', '0', '<', 's0')
tm.rule('s0', '1', '1', '<', 's0')
tm.rule('s0', '*', '1', '>', 'Return')
tm.rule('s0', '_', '0', '>', 'Return')

tm.rule('s1', '0', '0', '<', 's1')
tm.rule('s1', '1', '1', '<', 's1')
tm.rule('s1', '*', '1', '<', 's2fin')
tm.rule('s1', '_', '1', '>', 'Return')

tm.rule('s2', '0', '0', '<', 's2')
tm.rule('s2', '1', '1', '<', 's2')
tm.rule('s2', '_', '0', '<', 's2fin')
tm.rule('s2', '*', '1', '<', 's2fin')

tm.rule('s2fin', '_', '*', '>', 'Return')

tm.rule('Return', '0', '0', '>', 'Return')
tm.rule('Return', '1', '1', '>', 'Return')
tm.rule('Return', '+', '+', '>', 'Return')
tm.rule('Return', '=', '=', '>', 'Return')
tm.rule('Return', '_', '_', '>', 'Return')
tm.rule('Return', ';', ';', '<', 'det')

tm.rule('Fin', '0', '0', '<', 'Fin')
tm.rule('Fin', '1', '1', '<', 'Fin')
tm.rule('Fin', '+', '+', '<', 'Fin')
tm.rule('Fin', '_', '_', '<', 'Fin')
tm.rule('Fin', '=', '=', '<', 'Finito')

tm.rule('Finito', '_', '_', 'S', 'Finito')
tm.rule('Finito', '*', '1', 'S', 'Finito')
tm.rule('Finito', '0', '0', '<', 'Finito')
tm.rule('Finito', '1', '1', '<', 'Finito')


tm.validate('01+=_*;', ('q0', 'fin_r0', 'fin_r1', 'fin_l0', 'fin_l1', 'fin_l2', 's0', 's1', 's2', 's2fin', 'Return', 'det', 'g0', 'g1', 'Fin', 'Finito'))
tm.run('=100100001P+101001;', 0)
