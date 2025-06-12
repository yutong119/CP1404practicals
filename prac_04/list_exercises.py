numbers = []
for i in range(1, 6, 1):
    number = int(input(f"Please enter number{i}:"))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the number is {sum(numbers)/5}")