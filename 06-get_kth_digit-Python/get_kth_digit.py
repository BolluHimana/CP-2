# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	
	n=abs(digit)
	x=n%10**(k+1)
	y=n%10**(k)
	return(int(x-y)/10**k)
