from prac_09.car import Car
import random

class UnreliableCar(Car):
    """Assess whether one can drive a car through risk"""
    def __init__(self, name, fuel, reliability):
        """Initialize name, fuel, reliability"""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Determine whether it can be driven by checking if the risk assessment value is less than reliability;
        otherwise, return 0"""
        risk = random.randint(0, 100)
        if risk < self.reliability:
            return super().drive(distance)
        else:
            return 0





