#Area of a circle is to be calculated
#area=pi*r*r
import math
r=float(input("Enter the radius of the circle:"))
area=(math.pi*(r*r))
#ro=round(area,2)
#print("Area of the circle with radius ",r," is ",ro)
print("Area of the circle with radius ",r," is %.2f"%area)
