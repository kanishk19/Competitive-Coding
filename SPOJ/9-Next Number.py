a,b,c = map(int, raw_input().split())
while a!=0 or b!=0 or c!=0:
	if (b-a) == (c-b):
		print 'AP', (c+(c-b))
	else:
		print 'GP', (c*(c/b))
	a,b,c = map(int, raw_input().split())