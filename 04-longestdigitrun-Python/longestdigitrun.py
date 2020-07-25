# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	dict1={}
	n=abs(n)
	q=list(map(int,str(n)))
	c=1
	m=len(q)
	for i in range(m-1):
		if q[i]==q[i+1]:
			c=0
			if q[i] not in dict1:
				dict1[q[i]]=1
			else:
				dict1[q[i]]=dict1[q[i]]+1
	dict2={}
	if c==1:
		q.sort()
		return q[0]
	r=sorted(dict1.keys())
	for i in r:
		dict2[i]=dict1[i]
	dict2=sorted(dict2.items(),key=lambda item:item[1],reverse=True)
	return dict2[0][0]
