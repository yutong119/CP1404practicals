"""
emails
Estimate: 60 minutes
Actual:    minutes
"""
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

