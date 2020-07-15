# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):

	dist1=(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)))
	dist2=(math.sqrt(math.pow(x3-x2,2)+math.pow(y3-y2,2)))
	dist3=(math.sqrt(math.pow(x1-x3,2)+math.pow(y1-y3,2)))
	if(math.isclose(pow(dist1,2),(pow(dist2,2)+pow(dist3,2)))):
		return True

	elif(math.isclose(pow(dist2,2),(pow(dist1,2)+pow(dist3,2)))):
		return True

	elif(math.isclose(pow(dist3,2),(pow(dist1,2)+pow(dist2,2)))):
		return True
		
	else:
		return False

