test_cases = int (raw_input())
while test_cases>0:
	x_pos, y_pos = map(int, raw_input().split())
	result = x_pos + y_pos	
	if (x_pos & 1) and (y_pos & 1) and abs(x_pos - y_pos)<3 and x_pos>=y_pos:
		print result-1
	elif (x_pos%2==0) and (y_pos%2==0) and abs(x_pos - y_pos)<3 and x_pos>=y_pos:
		print result
	else:
		print 'No Number'
	test_cases-=1