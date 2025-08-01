from prac_09.unreliable_car import UnreliableCar

text_car_1 = UnreliableCar("1", 100, 30)
total_drives = 100
successful_times = 0

for i in range(total_drives):
    # Try to make the unreliable car text_car_1 travel 10 kilometers and return the actual distance traveled
    distance = text_car_1.drive(10)
    # 30% distance = 10, 70% distance = 0
    if distance > 0:
        successful_times += 1

print(successful_times)






