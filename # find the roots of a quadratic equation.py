# find the roots of a quadratic equation
#ax^2+bx+c=0
#x=(-b+sqrt((b^2)-4ac))/2a
#x=(-b-sqrt((b^2)-4ac))/2a
from math import sqrt
print("The Quadratic Equation be ax^2+bx+c=0")
a=float(input("Enter the value of a :"))
b=float(input("Enter the value of b :"))
c=float(input("Enter the value of c :"))
print("Equation is ",a,'x^2+',b,'x+',c,'=0')
D=((b*b)-4*a*c)
if D>=0:
    x1=(-b-(sqrt(D)))/(2*a)
    x2=(-b+(sqrt(D)))/(2*a)
    print("One root is ",x1)
    print("Other root is ",x2)
else:
    print("Oops Complex Root")    
