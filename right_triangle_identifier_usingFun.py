# A simple program to check whether the sides entered are the sides of a Right angled triangle.
#get the three sides
# condition to check is the pythogorus theorm
#if A,B,C are the sides A=sqrt(B^2+C^2)
from math import sqrt
def is_righttri(A,B,C):
    A=float(A)
    B=float(B)
    C=float(C)
    sides=[A,B,C]
    sides.sort()
    if (sides[2])**2 ==(sides[0])**2 +(sides[1])**2 :
        return print("The triangle is a right triangle")
    else:
        return print("The triangle is not a right triangle")
    
is_righttri(5,4,3)    



