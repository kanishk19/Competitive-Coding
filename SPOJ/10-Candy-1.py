n = int(raw_input())
while n!=-1:
	a = []
	for i in range(0,n):
	 x = raw_input()
	 a.append(int(x))
	if sum(a)%len(a)!=0:
		print -1
	else:
		avg = sum(a)/len(a)
		ans = 0
		for x in a:
			ans+=abs(x-avg)
		print ans/2
	n = int(raw_input())