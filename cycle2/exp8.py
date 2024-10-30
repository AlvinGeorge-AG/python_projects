#to check whether the given number is a krishnamurthi number
from math import factorial
numb=input("Enter the number :")
t=0
y=list(numb)
for i in range(0,len(y)):
    z=factorial(int(y[i]))
    t=t+z
if t==int(numb):
    print("The given number is a krishnamurthi number.")   
else:
        print("The given number is not a krishnamurthi number.")   
         
# print(t)    