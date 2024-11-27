#Write a Python program to calculate the area of a circle, given the center and a point on the perimeter. Use a function to find the radius as the distance between two points.
#center be (a,b)
import math
a=float(input('Enter the x cordinate of center :'))
b=float(input('Enter the y cordinate of center :'))
center=(a,b)
x=float(input('Enter the x cordinate of a point on the perimeter :'))
y=float(input('Enter the y cordinate of a point on the perimeter :'))
point=(x,y)
def radius():
    radiuss=math.sqrt(((a-x)**2 )+((b-y)**2))
    return radiuss
print(radius())
