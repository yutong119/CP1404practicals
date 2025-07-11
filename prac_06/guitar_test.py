"""Test that the last two methods(get_age, is_vintage) work as expected."""
"""
Estimate time: 20min
Actual time: 20min
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1925, 100)
another_guitar = Guitar("Another Guitar", 2013, 900)
# if want to get 9, need to change 2013 to 2016, the get_age function has no problem

# Test the get age method
expected_age_gibson = 100
actual_age_gibson = gibson.get_age()
print(f"Another Guitar get_age() - Expected {expected_age_gibson}. Got {actual_age_gibson}")

expected_age_another = 9
actual_age_another = another_guitar.get_age()
print(f"Another Guitar get_age() - Expected {expected_age_another}. Got {actual_age_another}")

# Test the is vintage method
expected_vintage_gibson = True
actual_vintage_gibson = gibson.is_vintage()
print(f"Gibson L-5 CES is_vintage() - Expected {expected_vintage_gibson}. Got {actual_vintage_gibson}")

expected_vintage_another = False
actual_vintage_another = another_guitar.is_vintage()
print(f"Another Guitar is_vintage() - Expected {expected_vintage_another}. Got {actual_vintage_another}")