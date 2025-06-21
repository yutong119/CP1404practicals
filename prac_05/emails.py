"""
emails
Estimate: 25 minutes
Actual:    minutes
"""
email_to_name = {}
email = input("Email: ")
while email != "":
    user_name = email.split('@')[0]
    choice = input(f"Is your name {user_name}? (Y/n)")
    if choice == "Y" or choice == "":
        email = input("Email: ")
    else:
        user_name = input("Name: ")
        email = input("Email: ")
print(email_to_name)
