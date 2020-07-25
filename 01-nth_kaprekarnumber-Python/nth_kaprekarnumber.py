# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def Kaprekar(n):
    if n<=0:
        return False
    p=n*n
    if p<10:
        if p==n:
            return True
    a=math.ceil(math.log(p,10))
    c=1
    while c<a:
        m1=p%10**c
        m2=p//10**c
        if m1==0:
            c=c+1
            continue
        if m1+m2==n:
            return True
            break
        c=c+1
    return False
        
def fun_nth_kaprekarnumber(n):
    l=[]
    for i in range(100000):
        if Kaprekar(i):
            l.append(i)
    return l[n]