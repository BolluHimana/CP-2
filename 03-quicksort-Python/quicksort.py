"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	a=[]
	b=[]
	c=[]
	if len(array)>1:
		p=array[0]
		for i in array:
			if i<p:
				a.append(i)
			elif i==p:
				b.append(i)
			else:
				c.append(i)
		return sorted(a)+b+sorted(c)
	else:
		return array
