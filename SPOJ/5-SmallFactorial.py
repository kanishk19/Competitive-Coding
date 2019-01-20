def factorial(inputNumber):
	fact = 1
	for i in range(1,inputNumber+1):
		fact*=i
	return fact

test_cases = int(input())
while test_cases:
	inputNumber = int(input())
	print factorial(inputNumber)
	test_cases-=1