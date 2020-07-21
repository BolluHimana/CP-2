# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):

	length=len(s2)
	new=""
	i=0
	while(i<len(s1)):
		if(s1[i:i+length]==s2):
			new+=s3
			i=i+length
			
		else:
			new+=s1[i]
			i=i+1
	return new

