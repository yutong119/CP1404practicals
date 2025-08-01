from prac_09.silver_service_taxi import SilverServiceTaxi

test1 = SilverServiceTaxi("hi",100, 2)
test1.drive(18)
fare = test1.get_fare()

assert fare == 48.78, f"Expected fare $48.78, got ${fare:.2f}"
print(f"Test passed: Fare is ${fare:.2f}")