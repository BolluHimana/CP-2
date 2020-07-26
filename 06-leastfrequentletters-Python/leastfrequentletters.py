# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")
import string
def leastfrequentletters(s):
	a=len(s)
	if a==0:
		return ' '
	str1=s.lower()
	val=String.ascii_lowercase
	c1=1000
	s1=''
	i=0
	while i<26:
		c2=str1.count(val[i])
		if c1>c2>0:
			c1=c2
			s1=val[i]
		elif c1==c2:
			s1=s1+val[i]
		i=i+1
	if s1=='':
		return s1
	return s1

