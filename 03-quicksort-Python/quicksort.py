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
			if i>p:
				c.append(i)
			elif i<p:
				a.append(i)
			else:
				b.append(i)
		return sorted(c)+b+sorted(a)
	else:
		return array
