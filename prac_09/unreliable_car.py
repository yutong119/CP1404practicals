from prac_09.car import Car
import random

class UnreliableCar(Car):
    """"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        risk = random.randint(0, 100)
        if risk < self.reliability:
            return super().drive(distance)
        else:
            return 0





