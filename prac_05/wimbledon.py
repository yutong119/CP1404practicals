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

