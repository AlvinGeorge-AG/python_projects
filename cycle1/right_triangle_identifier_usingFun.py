# # A simple program to check whether the sides entered are the sides of a Right angled triangle.
# #get the three sides
# # condition to check is the pythogorus theorm
# #if A,B,C are the sides A=sqrt(B^2+C^2)
# from math import sqrt
# def is_righttri(A,B,C):
#     A=float(A)
#     B=float(B)
#     C=float(C)
#     sides=[A,B,C]
#     sides.sort()
#     if sides[0]==0 and sides[1]==0 and sides[2]==0:
#         p1="Error"   
#     elif (sides[2])**2 ==(sides[0])**2 +(sides[1])**2 :
#         p1= "The triangle is a right triangle" 
#     else:
#         p1 = "The triangle is not a right triangle"
#     return print(p1)   
    
# # is_righttri(5,4,3)    



f=ord('A')
print(f)