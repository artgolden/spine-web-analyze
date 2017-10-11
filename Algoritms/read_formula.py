from stack import Stack

def read_formula(formula):
	
	register = 0
	operation = None
	number = 0

	regStack = Stack()
	operStack = Stack()

	def calculate(reg, oper, num):
		operDict = {
			'+': (lambda x, y: x + y),
			'-': (lambda x, y: x - y),
			'*': (lambda x, y: x * y),
			'/': (lambda x, y: float(x) / y),
		}
		return operDict[oper](reg, num)

	formula += '_'
	for i in formula:
		# print i
		if i in "0123456789":
			if operation == None:
				register *= 10
				register += int(i)
			else:
				number *= 10
				number += int(i)
		else:
			# print "else", number
			if number != 0:
				# print register, number, operation
				register = calculate(register, operation, number)
				operation = None
				number = 0
			if i == '(':
				if operation is not None:
					regStack.push(register)
					operStack.push(operation)
					register = 0
					operation = None
			elif i == ')':
				# print operStack
				if operStack.len != 0:
					print  "reg =", register, "oper =", operation, "num =", number
					regStack.sprint()
					operStack.sprint()
					operation = operStack.pop()
					number = register
					register = regStack.pop()
					print  "reg =", register, "oper =", operation, "num =", number
					register = calculate(register, operation, number)
					operation = None
					number = 0
			elif i in "+-*/":
				operation = i
				# print "oper = ", operation
	return register

result = read_formula("5+6*7")
print "Result = ", result
	

