import math
#To import the 3 numerical integration methods as well as second derivative function
from Functions import *
#The function
def func(x):
    p = math.exp(-math.pow(x,2))
    return p
error = 0.001
a=0
b=1
#Finding the 2nd derivative at 0 which is maximum
term = abs(secndderv(a,0.01,func))

#Findinf no of terms for three methods
Nm = math.ceil(math.sqrt(pow((b-a),3)*term/(24*error)))

Nt = math.ceil(math.sqrt(pow((b-a),3)*term/(12*error)))

#4th derivative for fn is obtained as 12
Ns=  math.ceil(pow(pow((b-a),5)*12/(180*error),1/4))
#If N for simpson is odd make it even
if Ns%2==1:
    Ns = Ns+1

print("Result for Midpoint: ",midpoint(0,1,Nm,func))
print("Result for Trapezoidal: ",trapezoidal(0,1,Nt,func))
print("Result for Simpson: ",simpson(0,1,Ns,func))

#Result for Midpoint:  0.7462107961317495
#Result for Trapezoidal:  0.7464612610366895
#Result for Simpson:  0.7468553797909872