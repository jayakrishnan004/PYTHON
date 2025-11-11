import math

r = int(input("Enter the radius of circle:"))
#area = math.pi * r**2
area = math.pi * pow(r,2)
print(f"The area of the circle is {round(area,2)} sq. cm")