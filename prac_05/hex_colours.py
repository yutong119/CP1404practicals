HEXADECIMAL_COLOR_CODE={"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2",
                        "Cadet Grey": "#91a3b0", "CadetBlue": "#5f9ea0", "Daffodil": "#ffff31", "Dandelion": "#f0e130", "Earth Yellow": "#e1a95f"}
print(HEXADECIMAL_COLOR_CODE)

color_name = input("Enter the color name: ").title()

while color_name != "":
    try:
        print(color_name, "is", HEXADECIMAL_COLOR_CODE[color_name])
    except KeyError:
        print("The color name doesn't exist, try again")
    color_name = input("Enter the color name: ").title()
print("THE END")