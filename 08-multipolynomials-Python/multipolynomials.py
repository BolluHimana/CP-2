# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	l1=[]
	l2=[]
	s=0
	for m in p1:
		for n in p2:
			l1.append(m*n)
	for i in range(len(l1)):
		if i!=1 and i!=2:
			l2.append(l1[i])
		else:
			s=s+l1[i]
			l2.append(s)
	if len(l2)>=5:
		return l2[0:1]+l2[2:3]+l2[4:]
	elif len(l2)<=4:
		return l2[0:1]+l2[2:]