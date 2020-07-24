# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2



def isprime(n):
	if n>1:
		for i in range(2,n):
			if n%i!=0:
				return True
		return False
	else:
		return False
def fun_nth_additive_prime(n):
	m=1
	while(n>=0):
		if isprime(m) and additive(m):
			 n=n-1
		m=m+1
	return m-1
def additive(n):
	a=[]
	s=0
	if(isprime(n)):
		while(n>0):
			r=n%10
			a.append(r)
			n=n//10
		for i in a:
			s=s+i
		if isprime(s):
			return True
		else:
			return False

