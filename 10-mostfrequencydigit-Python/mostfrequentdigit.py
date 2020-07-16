# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def count(n,d):
	count=0
	if(n%10==d):
		count=count+1
	n=n//10
	return count
def mostfrequentdigit(n):
	max=0
	for d in range(0,9):
		x=count(n,d)
		if(x>max):
			max=x
	return max