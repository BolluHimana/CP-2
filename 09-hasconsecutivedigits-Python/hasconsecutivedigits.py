# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	
	n=abs(n)
	n=str(n)
	if(len(n)<=2):
		return False
	l=[i for i in n]
	for i in range(0,len(n)+1):
		if(l[i]==l[i+1]):
			return True
