#exercise 2 shopping cart program

item = input("Enter the item: ")
price = float(input("what is the price: "))
qty = int(input("Enter the quantity: "))
total = price * qty
print(f"you have bought {qty} of {item}/s")
print(f"total amount is : ${total}")