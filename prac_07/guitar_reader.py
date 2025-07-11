from prac_07.guitar import Guitar

def load_guitar_data():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars

def get_new_guitar():
    new_name = input("Enter a new guitar: ")
    while new_name != "":
        new_year = int(input("Enter the year of guitar: "))
        nuw_cost = float(input("Enter the cost of guitar: "))
        return Guitar(new_name, new_year, nuw_cost)

def save_new_guitars(guitars):
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}")

main()



