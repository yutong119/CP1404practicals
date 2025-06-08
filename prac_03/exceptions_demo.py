"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When I put string and float and 0
2. When will a ZeroDivisionError occur?
    When I input 0 to denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    yes
"""
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")


#change the code to avoid the possibility of a ZeroDivisionError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")











