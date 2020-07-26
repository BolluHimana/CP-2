# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(n):
    if ishappynumber(n):
        if prime(n):
            return True
    else:
        return False
def prime(n):
    if n>=2:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
    return False
def addition(p):
    s=0
    while p>0:
        r=p%10
        s=s+(r**2)
        p=p//10
    return s
def ishappynumber(n):
    l=[]
    while addition(n) not in list:
        r=addition(n)
        if r!=1:
            l.append(r)
            n=r
        else:
            return True
    return False
