#A program to find the sum of cosine series
#cosx=1-(x^2/2!)+(x^4/4!)-(x^6/6!)+...n
from math import factorial as f
from math import pi
n=int(input('Enter the value of n (Number of terms):'))
x=float(input('Enter the value of x :'))# x is in degree
u=x
x=x*(pi/180)
cosine =1
s=-1
for i in range(2,n+1,2):
    y=((s)*(x**i)/(f(i)))
    cosine+=y
    s*=-1
print(f'Cos({u})= ',cosine)    