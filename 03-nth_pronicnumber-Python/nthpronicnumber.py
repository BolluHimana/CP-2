# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math
def pronic(n):
	a=0
	while int(math.sqrt(n)) >=a:
		if n==a*(a+1):
			return True
		a=a+1
def nthpronicnumber(n):
	l=[]
	for i in range(3000):
		if pronic(i):
			l.append(i)
	return l[n-1]