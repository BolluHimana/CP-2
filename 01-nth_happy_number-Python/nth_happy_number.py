# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)
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
		
def fun_nth_happy_number(n):
	l=[]
	for i in range(50):
		if ishappynumber(i):
			l.append(i)
	return l[n]