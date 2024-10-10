#compute nCr
#nCr=(n!/(r!(n-r)!))
print("You are going to find nCr")
print("RULES")
print("* n and r should be a non negative integer")
print("* Value of r should be less than or equal to n")
n=int(input("Enter the value of n :"))
r=int(input("Enter the value of r :"))
from math import factorial
if n>0 and r<=n and n.is_integer() and r.is_integer():
    com=(factorial(n)/(factorial(r)*(factorial(n-r))))
    print(n,'C',r,' is',com)
else:
    print("Please follow the rules !!")    