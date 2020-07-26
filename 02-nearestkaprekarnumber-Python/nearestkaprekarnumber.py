# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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
def fun_nearestkaprekarnumber(n):
    h=math.ceil(n)-n
    l=n-math.floor(n)
    if Kaprekar(n):
        return n
    m2=n+h
    m1=n-l
    while True:
        if Kaprekar(m1):
            if Kaprekar (m2):
                if abs(m1-n) > abs(m2-n):
                    return m2
                    break
                else:
                    return m1
                    break
            else:
                return m1
                break
        if Kaprekar(m2):
            return m2
            break
        m1=m1-1
        m2=m2+1


    return 1