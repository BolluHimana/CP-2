# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def uglynumber(n):
    if n==0:
        return False
    for i in [2,3,5]:
        while n%i==0:
            n=n//i
    return n==1
def fun_nth_uglynumber(n):
    l=[]
    for i in range(3000):
        if uglynumber(i):
            l.append(i)
    return l[n+1]

