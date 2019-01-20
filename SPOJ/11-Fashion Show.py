test_cases = int(raw_input())
for t in range(0,test_cases):
	n = int(raw_input())
	girls = [int(x) for x in raw_input().split()]
	boys = list(map(int, raw_input().split()))
	girls.sort()
	boys.sort()
	ans = 0
	for g,b in zip(girls,boys):
		ans+=(g*b)
	print ans