MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convent_celsius_to_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        elif choice == "F":
            celsius = float(input("Celsius: "))
            fahrenheit = convent_fahrenheit_to_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convent_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def convent_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()