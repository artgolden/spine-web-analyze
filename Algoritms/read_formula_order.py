from stack import Stack

def read_formula(formula):
	
	register = 0
	operation = None
	number = 0
	# Level of dive inside of brackets. It is needed to properly pop form low level stacks. 
	bracketsCount = 0

	regStack = Stack()
	operStack = Stack()
	lowOperStack = Stack()
	lowRegStack = Stack()
	lowCountStack = Stack()

	def calculate(reg, oper, num):
		"""Function to calculate two numbers."""
		operDict = {
			'+': (lambda x, y: x + y),
			'-': (lambda x, y: x - y),
			'*': (lambda x, y: x * y),
			'/': (lambda x, y: float(x) / y),
		}
		return operDict[oper](reg, num)

	formula += '_'
	index = 0
	for i in formula:
		print  "*** i = ", i, "reg =", register, "oper =", operation, "num =", number,\
		 regStack.get(), operStack.get(), lowOperStack.get(), lowRegStack.get(), lowCountStack.get(), bracketsCount
		if i in "0123456789":
			if operation == None:
				register *= 10
				register += int(i)
			else:
				number *= 10
				number += int(i)
		else:
			# print "else", number
			if number != 0 and not (i in "*/"):
				# print register, number, operation
				register = calculate(register, operation, number)
				operation = None
				number = 0
			if i == '(':
				bracketsCount += 1
				if operation is not None:
					regStack.push(register)
					operStack.push(operation)
					register = 0
					operation = None
			elif i == ')':
				# Also testing for the level of brackets we are on. 
				if lowOperStack.len != 0 and lowCountStack.array[-1] == bracketsCount:
					lowCountStack.pop()
					operation = lowOperStack.pop()
					number = register
					register = lowRegStack.pop()
					register = calculate(register, operation, number)
					operation = None
					number = 0
				bracketsCount -= 1
				if operStack.len != 0 and formula[index + 1] not in "*/":
					operation = operStack.pop()
					number = register
					register = regStack.pop()
					register = calculate(register, operation, number)
					operation = None
					number = 0
			elif i in "+-":
				# Also testing for the level of brackets we are on. 
				if lowOperStack.len != 0 and lowCountStack.array[-1] == bracketsCount:
					lowCountStack.pop()
					operation = lowOperStack.pop()
					number = register
					register = lowRegStack.pop()
					register = calculate(register, operation, number)
					operation = i
					number = 0
				else:
					lowOperStack.push(i)
					lowCountStack.push(bracketsCount)
					operation = None
					lowRegStack.push(register)
					register = 0
			elif i in "*/":
				if operation and operation not in "*/":
					lowOperStack.push(operation)
					lowCountStack.push(bracketsCount)
					lowRegStack.push(register)
					operation = None
					register = number
					number = 0
					operation = i
				elif operation:
					register = calculate(register, operation, number)
					operation = i
					number = 0
				else:
					operation = i
			elif i == '_' :
				if lowOperStack.len != 0:
					lowCountStack.pop()
					operation = lowOperStack.pop()
					number = register
					register = lowRegStack.pop()
					register = calculate(register, operation, number)
				while operStack.len != 0:
					operation = operStack.pop()
					number = register
					register = regStack.pop()
					register = calculate(register, operation, number)
					operation = None
					number = 0
		index += 1
					
		# print  "\n********** i = ", i, "reg =", register, "oper =", operation, "num =", number,\
		#  regStack.get(), operStack.get(), lowOperStack.get(), lowRegStack.get(), lowCountStack.get(), bracketsCount

	return register

result = read_formula("50+10+(4-5)*(20+10*(3*4-5*7))*(3-2)*(2+1)")
print "Result = ", result
	

