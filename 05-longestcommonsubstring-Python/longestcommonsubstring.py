# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    l1=len(s1)
    new=""
    for i in range(l1):
        for j in range(i+1,l1+1):
            s3=s1[i:j]
            if s3 in s2:
                if len(s3)==len(new):
                    if s3<new:
                        new=s3
                elif len(s3)>len(new):
                    new=s3
    return new
