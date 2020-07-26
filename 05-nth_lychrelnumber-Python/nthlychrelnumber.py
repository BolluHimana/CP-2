# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reversed(n):
	new=0
	while n>0:
		r=n%10
		new=(new*10)+r
		n=n//10
	return new
def lyrche(n):
	for k in range(60):
		n=n+reversed(n)
		if palindrome(n):
			return False
	return True
def nthlychrelnumbers(n):
	a=[]
	for j in range(4000):
		if lyrche(j):
			a.append(j)
	return l[n]
def palindrome(n):
	return n==reversed(n)