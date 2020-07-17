# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	n=str(n)
	li=[int(i) for i in n]
	c=[]
	for  i in range(0,9):
		list.count(i)
		c.append(i)
	a=max(c)
	b=c.index(a)
	d=li[b]
	return d