# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	s1=""
	d=len(s)
	if n<0:
		n1=abs(n)
		n1=n1%d
		s1=s[d-n1:]+s[:d-n1]
		return s1
	if n>0:
		n=n%d
		s1=s[n:]+s[:n]
		return s1

	return s

