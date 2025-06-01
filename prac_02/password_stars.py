MIN_LENGTH = 6
def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    """print the asterisks as much as password"""
    print("*" * len(password))

def get_password(MIN_LENGTH):
    """get user password and error check"""
    password = input("Enter your password: ")
    while len(password) != MIN_LENGTH:
        print(f"The password must be {MIN_LENGTH}")
        password = input("Enter your password: ")
    return password

main()