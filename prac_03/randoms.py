import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
· What did you see on line 1?
    I saw a random number between 5 and 20
· What was the smallest number you could have seen, what was the largest?
    5 and 19
"""

"""
· What did you see on line 2?
    3， 5， 7， 9
· What was the smallest number you could have seen, what was the largest?
    3 and 9
· Could line 2 have produced a 4?
    No，starting from 3, the step taken is 2，only 5 can occur
"""

"""
What did you see on line 3?
    Floating-point numbers between 2.5 and 5.5
What was the smallest number you could have seen, what was the largest?
    2.557871326045258 and 5.238009578850847
"""

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,101))