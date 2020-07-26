# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	n=str(n)
	l=len(n)
	if(l==1):
		return int(n)
	elif(l==2):
		if n[0]>n[1]:
			return int(n[1])
		else:
			return int(n[0])
	else:
		c=0
		r=-1
		for i in range(l-1):
			if(n[i]==n[i+1]):
				r=n[i]
				c=c+1
		if c>0:
			return int(r)