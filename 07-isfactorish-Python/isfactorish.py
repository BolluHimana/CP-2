# Write the function fun_isfactorish(n) that takes a value int n, 
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits 
# (so no two digits are the same), where each of the digits is a factor of the number 
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)


def fun_isfactorish(n):
	n1=abs(n)
	temp=n1
	a=[]
	b=[]
	while temp>0:
		r=temp%10
		a.append(r)
		temp=temp//10
	if a[0]==a[1] or a[1]==a[2] or a[2]==a[0] or a.count(0)>0 or len(b)<3 or len(a)<3:
		return False
	for i in range(1,n1+1):
		if n1%i==0:
			b.append(i)
	for j in a:
		if j in b:
			return True


