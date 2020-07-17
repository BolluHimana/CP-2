# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	li=[]
	a=0
	while(n):
		a=n%10
		li.append(a)
		n=n//10
	c=[]
	for  i in range(0,9):
		m=li.count(i)
		c.append(m)
	a=max(c)
	b=c.index(a)
	d=li
