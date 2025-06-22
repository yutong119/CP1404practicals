"""
emails
Estimate: 30 minutes
Actual:   30 minutes
"""
def main():
    """Read file, get champion counts and arrange the champion countries in alphabetical order"""
    data = read_data()

    champion_counts = count_champions(data)
    print("Wimbledon Champions:")
    for name, count in champion_counts.items():
        print(f"{name} {count}")

    countries = get_countries(data)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_data():
    """Read the data from wimbledon.csv and return the list"""
    data = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            data.append(line.strip().split(','))
    return data

def count_champions(data):
    """Count the number of times the champion has won awards"""
    champion_counts = {}
    for row in data[1:]:
        champion = row[2]
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts

def get_countries(data):
    """The collection of countries to which the champion belongs"""
    countries = set()
    for row in data[1:]:
        countries.add(row[1])
    return sorted(countries)

main()
