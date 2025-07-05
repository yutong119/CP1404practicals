"""
Estimate time: 30min
Actual time:
"""
from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")

while name != "":
    year = input("Year: ")
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{Guitar(name, year, cost)} added.")
    name = input("Name: ")







