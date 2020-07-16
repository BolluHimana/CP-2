# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def pascal(row):
	l=[]
	for i in range(0,row+1):
		t=[]
		if(i==0) :
			t.append(1)
		if(i==1):
			for i in range(i+1):
				t.append(1)
		if(i>1):
			t.append(1)
			for k in range(0,len(l[i-1])-1):
				t.append(l[i-1][k]+l[i-1][k+1])
			t.append(1)	
		l.append(t)
	return l
	
def fun_pascaltrianglevalue(row, col):
	list = pascal(row)
	for i in range(len(list)) :
		if i==row:
			l=len(list[i])
			if col<l:
				return list[i][col]
			else:
				return 0