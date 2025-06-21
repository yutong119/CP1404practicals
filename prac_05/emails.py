"""
emails
Estimate: 25 minutes
Actual:   40 minutes
"""
def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        guessed_name = extract_name_from_email(email)
        confirmed_name = get_valid_name(email, guessed_name)
        email_to_name[email] = confirmed_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    guessed_name = email.split('@')[0]
    return guessed_name

def get_valid_name(email, guessed_name):
    choice = input(f"Is your name {guessed_name}? (Y/n)").lower()
    if choice == 'y' or choice == '':
        return guessed_name
    else:
        user_name = input("Name: ")
        return user_name

main()