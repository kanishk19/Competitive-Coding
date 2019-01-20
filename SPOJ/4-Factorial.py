def getZeroes(inputNUmber):
	ans, divisor= 0,5
	while divisor<=inputNUmber:
		ans+=(inputNUmber/divisor)
		divisor*=5
	return ans


test_cases = int(input())
while test_cases>0:
	inputNUmber = int(input())
	print getZeroes(inputNUmber)
	test_cases-=1