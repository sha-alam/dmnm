import numpy

x = [1,2,3,4,5,6,7,8]
y = [1,8,27,64,125,216,343,512]
m = 7.5
n= len(x)-1
t= (m-x[n])/(x[1]-x[0])
coeff=t
k=1
sum=y[n]

for i in range(n,1,-1):
    y= numpy.diff(y)
    sum= sum+ coeff*y[i-1]
    coeff= coeff*(t+k)/(k+1)
    k=k+1

print( "the value is :", sum)