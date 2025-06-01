total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <0:
    print("Invalid number of items !")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    single_price = float(input("Price of item:"))
    total_price = total_price + single_price
print(f"Total price for {number_of_items} items is {total_price}")
