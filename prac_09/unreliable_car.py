from prac_09.car import Car
import random

class UnreliableCar(Car):
    """"""
    def __init__(self, **kwargs, reliability: float):
        super()__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):



