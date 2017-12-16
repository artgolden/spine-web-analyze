from stack import Stack

def read_formula(formula):
	
	register = 0
	operation = None
	number = 0
	# Level of dive inside of brackets. It is needed to properly pop form low level stacks. 
	bracketsCount = 0

	regStack = Stack()
	operStack = Stack()
	countStack = Stack()
	
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

	def brackets_stack_pop_calc(reg, operStack, regStack, countStack):
		"""Extrack from brackets stack, calculate and put in register"""
		countStack.pop()
		oper = operStack.pop()
		num = reg
		reg = regStack.pop()
		reg = calculate(reg, oper, num)
		oper = None
		num = 0
		return oper, reg, num

	def low_stack_push(oper, reg, count, lowCountStack, lowOperStack, lowRegStack):
		lowOperStack.push(oper)
		lowRegStack.push(reg)
		lowCountStack.push(count)

	def low_stack_pop_calc(reg, lowCountStack, lowOperStack, lowRegStack):
		"""Extrack from low operations stack, calculate and put in register"""
		lowCountStack.pop()
		oper = lowOperStack.pop()
		num = reg
		reg = lowRegStack.pop()
		reg = calculate(reg, oper, num)
		return oper, reg, num



	formula += '_'
	index = 0
	for i in formula:
		print  "*** i = ", i, "reg =", register, "oper =", operation, "num =", number,\
		 regStack.get(), operStack.get(), countStack.get(), lowOperStack.get(), lowRegStack.get(), lowCountStack.get(), bracketsCount
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
					# Push current operation with number to bracket's stack
					regStack.push(register)
					operStack.push(operation)
					countStack.push(bracketsCount)
					register = 0
					operation = None
			elif i == ')':
				# Also testing for the level of brackets we are on. 
				if lowOperStack.len != 0 and lowCountStack.array[-1] == bracketsCount:
					operation, register, number, = low_stack_pop_calc(register, lowCountStack, lowOperStack, lowRegStack)
					operation = None
					number = 0
				if operStack.len != 0 and formula[index + 1] not in "*/" and countStack.array[-1] == bracketsCount:
					operation, register, number = brackets_stack_pop_calc(register, operStack, regStack, countStack)
				bracketsCount -= 1

			elif i in "+-":
				# Also testing for the level of brackets we are on. 
				if lowOperStack.len != 0 and lowCountStack.array[-1] == bracketsCount:
					operation, register, number, = low_stack_pop_calc(register, lowCountStack, lowOperStack, lowRegStack)
					operation = i
					number = 0
				else:
					low_stack_push(i, register, bracketsCount, lowCountStack, lowOperStack, lowRegStack)
					operation = None
					register = 0

			elif i in "*/":
				if operation and operation not in "*/":
					low_stack_push(operation, register, bracketsCount, lowCountStack, lowOperStack, lowRegStack)
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
					operation, register, number, = low_stack_pop_calc(register, lowCountStack, lowOperStack, lowRegStack)
				
				while operStack.len != 0:
					operation, register, number = brackets_stack_pop_calc(register, operStack, regStack, countStack)
		index += 1
					
	return register

formula = "(2*(2+1)*(1+(3+4))*(1+(4+6)+3))"
result = read_formula(formula)
print "Result = ", result

print "Reference = ", eval(formula)
	

