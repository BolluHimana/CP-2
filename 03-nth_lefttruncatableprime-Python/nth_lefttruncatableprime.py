# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math
def LeftTruncatablePrime(n):
    if str(n).__contains__("0") or prime(n)==False:
        return False
    else:
        c1=digitcount(n)
        for i in range(1,c1):
            p=n%(10**i)
            if prime(p)==False:
                return False
        return True
def prime(n):
    if n>=2:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
    return False
def digitcount(n):
    num=abs(n)
    c=1
    while num>10:
        num=num//10
        c=c+1
    return c

def fun_nth_lefttruncatableprime(n):
    l=[]
    for i in range(5000):
        if LeftTruncatablePrime(i):
            l.append(i)
    return l[n]