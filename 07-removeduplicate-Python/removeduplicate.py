# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	c=[i for i in text]
	c1=list(dict.fromkeys(c))
	s=""
	for i in c1:
		s=s+i
	return s