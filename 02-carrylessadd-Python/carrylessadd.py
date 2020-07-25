# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

import math
def fun_carrylessadd(x, y):
	
	p=1
	ind=0
	add=0
	
	if(y==0):
		return x
	elif(x==0):
		return y

	while(y or x):
		ind=((y%10)+(x%10))
		ind=ind%10
		add=(ind*p)+add
		p=p*10
		y=math.floor(y/10)
		x=math.floor(x/10)
	a=str(add)
	a.strip("0")
	return int(a)

