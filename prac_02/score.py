import random
def main():
    score = get_valid_score()
    category = category_score(score)
    print(f"Your score is {category}")

    random_score = random.randint(1, 100)
    random_category = category_score(random_score)
    print(f"The random score {random_score} is classify {random_category}")

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("The score must between 0 and 100")
        score = float(input("Enter score: "))
    return score

def category_score(prompt):
    if prompt < 50:
        category = "bad"
    elif prompt < 90:
        category = "pass"
    elif prompt <= 100:
        category = "excellent"
    return category

main()