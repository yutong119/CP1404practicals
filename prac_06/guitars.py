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

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    # do something with i (the index) and guitar (the element)

    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")





