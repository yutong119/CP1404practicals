"""
emails
Estimate: 25 minutes
Actual:    minutes
"""
email_to_name = {}
email = input("Email: ")
while email != "":
    guessed_name = email.split('@')[0]

    choice = input(f"Is your name {guessed_name}? (Y/n)")
    if choice == "Y" or choice == "":
        email_to_name[email] = guessed_name
    else:
        user_name = input("Name: ")
        email_to_name[email] = user_name

for email, name in email_to_name.items():
    print(f"{name} ({email})")
