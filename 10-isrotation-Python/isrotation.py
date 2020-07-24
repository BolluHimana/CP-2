# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	a=str(x)
	b=str(y)
	if len(a)!=len(b):
		return False
	if a=="".join(reversed(b)):
		return True
	if b in a*2:
		return True
