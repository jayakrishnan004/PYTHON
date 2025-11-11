#temperature converter

unit = input("is this temperature in celcius or fahrenheit (c / f)")
temp = float(input("Enter the temperature:"))

if unit == "f":
    result = (5/9)*(temp - 32)
    print(f"The temperature is {round(result,1)} degree celcius.")
elif unit == "c":
    result = ((9/5)*temp) +32
    print(f"The temperature is {round(result,1)} degree fahrenheit.")
else:
    print(f"{unit} is not a known unit")