#For importing monte carlo code
from Functions import *
#The function
def func(x):
    p = 4/(1+pow(x,2))
    return p
#m gives no of iterations
m=0
i=0
Value=[]
while i<10000:
    m +=10
    #Calling code from library
    a = montecarlo(0, 1, m,func)
    print(a)
    Value.append(a)
    i+=1
#At iteration number 100000 value of pi is obtained as 3.144094
