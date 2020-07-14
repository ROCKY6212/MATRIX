from numpy import *
m1=matrix('1 2 3;1 2 3;1 2 3')
m2=matrix('1 2 3;1 2 3;1 2 3')
k,l,m=0,0,0
a,b,c=0,0,0
p,q,r=0,0,0
for i in range(3):
    for j in range(3):
        if i==1:
            a += m1[i, j] * m2[j, 0]
            b += m1[i, j] * m2[j, 1]
            c += m1[i, j] * m2[j, 2]
        elif i==2:
            p += m1[i, j] * m2[j, 0]
            q += m1[i, j] * m2[j, 1]
            r += m1[i, j] * m2[j, 2]
        else:
            k += m1[i, j] * m2[j, 0]
            l += m1[i, j] * m2[j, 1]
            m += m1[i, j] * m2[j, 2]
arr1=array([[k,l,m],[a,b,c],[p,q,r]])
m3=matrix(arr1)
print(m3)
m4=m1*m2
print(m4)
