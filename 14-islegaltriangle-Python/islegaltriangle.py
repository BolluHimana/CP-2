# islegaltriangle(s1, s2, s3)
# Write the function islegaltriangle(s1, s2, s3) that takes three int or float values representing
# the lengths of the sides of a triangle, and returns True if such a triangle exists and False
# otherwise. Note from the triangle inequality that the sum of each two sides must be greater
# than the third side, and further note that all sides of a legal triangle must be positive. Hint:
# how can you determine the longest side, and how might that help?

def islegaltriangle(s1, s2, s3):
	if(s1>0 and s2>0 and s3>0):
		large=max(s1,s2,s3)
		
		if(s1<s2+s3 and s2<s1+s3 and s3<s1+s2):
				return True
		else:
				return False
	else:
		return False
