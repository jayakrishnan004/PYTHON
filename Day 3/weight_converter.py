#python weight converter

weight = float(input("Enter your weight :"))
unit = input("kilograms or pounds (k or p):")

if unit == ("k"):
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight,3)} {unit}")
elif unit == ("p"):
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight,3)} {unit}")
else:
    print(f" {unit} is not a known unit")

