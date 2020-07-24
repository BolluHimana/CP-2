# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.
import math
def findzerowithbisection(x, epsilon):
	m=(x+1)/2
	if(findzerowithbisection(1,epsilon)*findzerowithbisection(m,epsilon)<0):
		n=(1+m)/2
		findzerowithbisection(n,epsilon)
	elif(findzerowithbisection(m,epsilon)*findzerowithbisection(x,epsilon)<0):
		n=(m+x)/2
		findzerowithbisection(n,epsilon)
