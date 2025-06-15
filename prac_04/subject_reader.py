"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list.append(parts)  # Add the processed row of data (in list form) to the total list
    input_file.close()
    return data_list

def display_subject_details(data):
    """Display detailed subject information."""
    for item in data:
        subject_code, lecturer, student_number = item
        print(f"{subject_code} is taught by {lecturer} and has {student_number} students")

main()