from prac_07.guitar import Guitar

def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')

    in_file.close()