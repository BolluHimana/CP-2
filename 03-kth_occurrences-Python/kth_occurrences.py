# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dict1={}
	c=0
	for i in s:
		if i not in dict1.keys():
			dict1[i]=1
		else:
			dict1[i]=dict1[i]+1
	dict2={k:v for k,v in sorted(dict1.items(),key=lambda item:item[1])}
	l=[{dict1[k]:k}for k in dict1]
	l.reverse()
	a=l[n-1].values()
	r=l(a)[0]
	return r


