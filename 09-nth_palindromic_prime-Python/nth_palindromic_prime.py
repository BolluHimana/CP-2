# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2



def isprime(n):
	if n>1:
		for i in range(2,n):
			if n%i==0:
				return False
		return True
	else:
		return False
def palindrome(n):
	s=0
	temp=n
	while(n>0):
		r=n%10
		s=s*10+r
		n=n//10
	if sum!=temp:
		return False
	return True
def fun_nth_palindromic_prime(n):
	m=1
	while n>=0:
		if isprime(m):
			if palindrome(n):
				n=n-1
		m=m+1
	return m-1