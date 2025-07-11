from prac_07.guitar import Guitar

def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)
    in_file.close()