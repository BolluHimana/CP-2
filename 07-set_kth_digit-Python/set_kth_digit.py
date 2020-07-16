# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	dig = list(str(n))
	# print (split(nString))
	# nChar = [c for c in dig]
	# # print (nChar)
	# nReverse = list(reversed(nChar))
	# # print (nReverse)
	# if(k>=len(dig)):
	# 	nReverse=nReverse+d
	# ele=nReverse[k]
	# newRev = list(reversed(nReverse))
	if(n<0):
		if k<len(dig):
			dig[len(dig)-1-k]=str(d)
			dig.insert(0,"-")
			return int("".join(dig))
		else:
			dig.insert(0,str(d))
			dig.insert(0,"-")
			return int("".join(dig))
	else:
		if k<len(dig):
			dig[len(dig)-1-k]=str(d)
			return int("".join(dig))
		else:
			dig.insert(0,str(d))
			return int("".join(dig))




			

