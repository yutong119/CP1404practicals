import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print(" ".join(f"{num:2}" for num in numbers))



