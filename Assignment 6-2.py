from Functions import *

#Defining the function
def func(x):
    p = x/(x+1)
    return p
#The limits of integration
b=3
a=1
#The result for N=6
print("Itr    Midpoint Method    Trapezoidal Method  Simpson's Method  Analytical result")
print("N=6 =>",midpoint(1,3,6,func),trapezoidal(1,3,6,func),simpson(1,3,6,func),1.306852)
#The result for N=10
print("N=10=>",midpoint(1,3,10,func),trapezoidal(1,3,10,func),simpson(1,3,10,func),1.306852)
#The result for N=24
print("N=24=>",midpoint(1,3,24,func),trapezoidal(1,3,24,func),simpson(1,3,24,func),1.306852)
#The analytical result is 1.306852
#Itr    Midpoint Method    Trapezoidal Method  Simpson's Method  Analytical result
#N=6 => 1.3051226551226551 1.3051226551226551 1.3068302068302067 1.306852
#N=10=> 1.3062285968245722 1.3062285968245722 1.3068497693110697 1.306852
#N=24=> 1.3067443360227213 1.3067443360227213 1.3068527256556821 1.306852
