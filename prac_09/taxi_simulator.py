from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi
MENU = """
q)uit, c)hoose taxi, d)rive"""

def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = get_valid_choice()
    while choice != 'q':
        if choice == 'c':
            print(f"Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")

        elif choice == 'd':



def get_valid_choice():
    choice = input(">>>")
    if choice not in ['q', 'c', 'd']:
        print("Invalid choice")
    else:
        return choice



