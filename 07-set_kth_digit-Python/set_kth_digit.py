# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	dig = str(n)
	dChar = str(d)
	# print (split(nString))
	nChar = [c for c in dig]
	# print (nChar)
	nReverse = reversed(nChar)
	# print (nReverse)
	if(k>=len(dig)):
		nReverse=nReverse+dChar
	ele=nReverse[k]
	newRev = reversed(nReverse)
	s=""
	if(n<0) :
		s=s+"-"
		for i in range(len(dChar)):
			if(dChar[i]!=ele):
				s=s+dChar[i]
			if( dChar[i]==ele):
				s=s+d	
	else:
		for i in range(len(dChar)):
			if(dChar[i]!=ele):
				s=s+dChar[i]
			if( dChar[i]==ele):
				s=s+d
	
