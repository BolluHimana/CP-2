# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def powerful(n):
	a=2
	while n>=2:
		if n%a==0:
			if n%(a**2)!=0:
				return False
			while n%a==0 and n>=2:
				n=n//a
		else:
			a=a+1
	return True
def nthpowerfulnumber(n):
	l=[]
	for i in range(2000):
		if powerful(i):
			l.append(i)
	return l[n+1]
