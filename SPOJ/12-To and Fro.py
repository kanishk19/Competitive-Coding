col_size = int(input())
while col_size!=0:
	mo_msg = input()
	row_size = len(mo_msg)//col_size
	k = 0
	# msg_2D = [['']*col_size]*row_size
	msg_2D = []
	flag = True
	for i in range(0,row_size):
		msg_1D = []
		if flag:
			for j in range(0,col_size):
				msg_1D.append(mo_msg[k])
				k+=1
		else:
			for j in range(col_size-1,-1,-1):
				msg_1D.append(mo_msg[k])
				k+=1
			msg_1D = msg_1D[::-1]
		msg_2D.append(msg_1D)
		flag = not flag
		
	for j in range(col_size):
		for i in range(row_size):
			print(msg_2D[i][j], end='')
	print('')
			
	col_size = int(input())