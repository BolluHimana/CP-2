# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    a=len(m1[0])
    l1=len(m2)
    l=[]
    if(a==l1):
        for i in range(0,len(m1)):
            t=[]
            for j in range(0,len(m2[0])):
                n=0
                for k in range(0,a):
                    n=n+m1[i][k]*m2[k][j]
                t.append(n)
            l.append(t)
        return l
    else:
        return None