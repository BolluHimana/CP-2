# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):

	for i in range(len(l)):
		for j in range(len(l[i])):
			
			n=l[i][j]
			m=1
			c=0
			while(n>=m):
				if n%m==0:
					c=c+1
					m=m+1
				else:
					m=m+1
			if(c<=2):
				return False
				
	return True

