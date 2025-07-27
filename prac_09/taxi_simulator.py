from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi
MENU = """
q)uit, c)hoose taxi, d)rive"""

def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = get_valid_choice()
    while choice != 'q':
        if choice == 'c':
            print(f"Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")
            choice = get_valid_choice()

        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
                print(f"Bill to date: ${total_bill}")
                choice = get_valid_choice()
            else:
                print("You need to choose a taxi before you can drive")\
                print(f"Bill to date: ${total_bill}")
                choice = get_valid_choice()

    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)

def get_valid_choice():
    choice = input(">>>")
    while choice not in ['q', 'c', 'd']:
        print("Invalid choice")
        choice = input(">>>")
    return choice

main()

