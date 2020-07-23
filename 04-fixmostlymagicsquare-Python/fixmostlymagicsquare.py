# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	l=[]
	a=[]
	p=0
	q=0
	result=0
	result1=0
	for i in L:
		s=0
		for j in i:
			s=s+j
		l.append(s)
	for i in range(len(l)):
		if(l.count(l[i])==1):
			p=i
			result1=l[i]
		if(l.count(l[i]>1)):
			result=l[i]
	for i in range(len(L)):
		s=0
		for j in range(len(L)):
			s=s+L[j][i]
		a.append(s)
		for i in range(len(a)):
			if(a.count(a[i]==1)):
				q=i
	final=result1-result
	if(result>0):
		L[p][q]=L[p][q]-final
	else:
		L[p][q]=L[p][q]+final
	return L
	
