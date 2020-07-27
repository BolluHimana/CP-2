# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
def add(n):
    a=0
    while n>0:
        r=n%10
        a+=r
        n=n//10
    return a
def factorsSum(n):
    l1=[]
    while n%2==0:
        l1.append(2)
        n=n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            l1.append(i)
            n=n/1
    if n>=3:
        l.append(n)
    a=0
    for i in l1:
        length=len(str(i))
        if length==1:
            a=a+i
        elif i is not n and length>1:
            a+=add(i)
    return a
def smith(n):
    if factorsSum(n)==add(n):
        return True
    else:
        return False
def fun_nth_smithnumber(n):
    list1=[]
    for i in range(1,1000):
        if not prime(i)  and smith(i):
            list1.append(i)
    return list1[n-1]