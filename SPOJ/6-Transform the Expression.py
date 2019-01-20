def isOperand(character):
	return character == '+' or character =='-' or character == '*' or character == '/' or character == '^'


def reversePolish(inputString):
	result = ''
	stack = []
	for i in inputString:
		if isOperand(i):
			stack.append(i)
		elif i == ')':
			result+=(stack.pop())
		elif i == '(':
			continue
		else:
			result+=(i)
	return result


test_cases = int(input())
while test_cases>0:
	inputString = raw_input()
	print reversePolish(inputString)
	test_cases-=1