# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def find(n):
	sum=0
	while(n>0):
		a=n%10
		sum=sum+(a)*(a)
		n=n//10
	return sum
def ishappynumber(n):
	if(n<=0):
		return False
	sum=n
	while(sum!=1 and sum!=4):
		sum=find(sum)
	if(sum==1):
		return True
	else:
		return False
def isprime(n):
	if(n>1):
		for i in range(2,n):
			if((n%i)!=0):
				return True
			else:
				return False
				
def fun_nth_happy_prime(n):
	l=[]
	for i in range(100):
		if(ishappynumber(i)):
			if(isprime(i)):
				l.append(i)
	return l[n]