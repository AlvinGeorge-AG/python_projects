# A simple program to check whether the sides entered are the sides of a Right angled triangle.
#get the three sides
# condition to check is the pythogorus theorm
#if A,B,C are the sides A=sqrt(B^2+C^2)
def rtriangle():

    A=float(input("Enter the length of side A :"))
    B=float(input("Enter the length of side B :"))
    C=float(input("Enter the length of side C :"))
    from math import sqrt
    R="The Triangle is a Right Triangle"
    if A==sqrt(B**2 + C**2):
         R="The Triangle is a Right Triangle"
    elif B==sqrt(A**2 + C**2):
         R="The Triangle is a Right Triangle"   
    elif C==sqrt(A**2 + B**2):
         R="The Triangle is a Right Triangle"
    else:
        R="The Triangle is NOT a Right Triangle"
    return R
print(rtriangle())    