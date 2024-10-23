#to find the digits in the factorial of 1000
from math import factorial
f=factorial(1000)
# print(f)
f_str=str(f)
length=len(f_str)
print(length)
no_of_0s=f_str.count('0')
print(no_of_0s)