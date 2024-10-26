# A simple program to check whether the sides entered are the sides of a Right angled triangle.
#get the three sides
# condition to check is the pythogorus theorm
#if A,B,C are the sides A=sqrt(B^2+C^2)
from math import sqrt
A=float(input("Enter first side A :"))
B=float(input("Enter second side B :"))
C=float(input("Enter third side C :"))
if A==sqrt(B*B+C*C):
    print("The Triangle is a Right triangle")
elif B==sqrt(A*A+C*C):
    print("The Triangle is a Right triangle")
elif C==sqrt(B*B+A*A):
    print("The Triangle is a Right triangle") 
else:
    print("The Triangle is not a right triangle ")       