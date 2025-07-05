"""Test that the last two methods(get_age, is_vintage) work as expected."""
from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1925, 100)
another_guitar = Guitar("Another Guitar", 2013, 900)

# Test the get age method
expected_age_gibson = 100
actual_age_gibson = gibson.get_age()
print(f"Another Guitar get_age() - Expected {expected_age_gibson}. Got {actual_age_gibson}")

expected_age_another = 9
actual_age_another = another_guitar.get_age()
print(f"Another Guitar get_age() - Expected {expected_age_another}. Got {actual_age_another}")

