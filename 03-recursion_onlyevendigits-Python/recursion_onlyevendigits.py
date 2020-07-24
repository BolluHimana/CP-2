# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
	a=len(l)
	if(a==0):
		return []
	else:
		if(even(l[0])!=""):
			return [int(even(l[0]))]+fun_recursion_onlyevendigits(l[1:])
		else:
			return[0]+fun_recursion_onlyevendigits(l[1:])
			
def even(n):
	if(n>0):
		if(((n%10)%2)!=0):
			return even(n//10)
		else:
			return (even(n//10)+str(n%10))
	else:
		return ""