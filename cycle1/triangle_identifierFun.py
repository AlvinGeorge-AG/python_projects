A=[1,3,4,5,5,4,6,7,33,878,77,22]
A.sort()
# print(A)
# import right_triangle_identifier_usingFun
# # is_righttri(5,4,3)
# right_triangle_identifier_usingFun.is_righttri(6,8,10)
from right_triangle_identifier_usingFun import is_righttri
is_righttri(13,12,5)







# # A simple program to check whether the sides entered are the sides of a Right angled triangle.
# #get the three sides
# # condition to check is the pythogorus theorm
# #if A,B,C are the sides A=sqrt(B^2+C^2)
# from math import sqrt
# A=float(input("Enter first side A :"))
# B=float(input("Enter second side B :"))
# C=float(input("Enter third side C :"))
# if A==sqrt(B*B+C*C):
#     print("The Triangle is a Right triangle")
# elif B==sqrt(A*A+C*C):
#     print("The Triangle is a Right triangle")
# elif C==sqrt(B*B+A*A):
#     print("The Triangle is a Right triangle") 
# else: