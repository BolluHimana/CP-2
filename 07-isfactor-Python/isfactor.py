# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	if(n%f==0 or (n==0 and f>0)):
		return True
	else:
		return False # replace with your solution
