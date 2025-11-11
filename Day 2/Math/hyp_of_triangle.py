import math

a = float(input("Enter the side a of the right angled triangle : "))
b = float(input("Enter the side b of the right angled triangle : "))

hypotenuse = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse is {round(hypotenuse,2)}")