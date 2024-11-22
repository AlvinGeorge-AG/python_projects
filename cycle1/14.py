#to find the digits in the factorial of 1000
from math import factorial
f=factorial(1000)
# print(f)
f_str=str(f)
length=len(f_str)
print('Total number of digits :',length)
no_of_0s=f_str.count('0')
print('Total number of zeros :',no_of_0s)