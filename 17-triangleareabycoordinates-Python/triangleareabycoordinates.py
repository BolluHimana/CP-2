# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math

def trianglearea(dist1, dist2, dist3):
	s=(dist1+dist2+dist3)/2
	a=math.sqrt((s)*(s-dist1)*(s-dist2)*(s-dist3))
	return a
def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	dist1=(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)))
	dist2=(math.sqrt(math.pow(x3-x2,2)+math.pow(y3-y2,2)))
	dist3=(math.sqrt(math.pow(x1-x3,2)+math.pow(y1-y3,2)))
	trianglearea(dist1,dist2,dist3)
	