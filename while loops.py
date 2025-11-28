#while loop
#execute some code WHILE some condition remains true


# name = input("Enter your name: ")
# while name =="":
#     print(f"You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Your name is {name}")


# age = int(input("What is your age? "))
# while age<0:
#     print(f"age cant be negative")
#     age = int(input("What is your age? "))
# print(f"your age is {age}")

# #use some logical operators...
# food = input("Enter a food you like(q to quit):")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("enter another food you like(q to quit):")
# print("ok bye")


#use or operator
num = int(input("Enter a number between 1 - 10 : "))
while num<1 or num>10:
    print(f"number is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")