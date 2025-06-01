def main():
    score = 0
    print("Menu: ")
    choice = input("> " ).upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == 0:
                print("Please enter a score first")
            else:
                result = print_result(score)
                print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell")

def get_valid_score():
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score, please try again")
        score = float(input("Enter your score: "))
    return score

def print_result(score):
    if score < 50:
        result = "bad"
    elif score < 90:
        result = "pass"
    elif score <= 100:
        result = "excellent"
    return result

def print_stars(score):
    print("*" * int(score))

main()