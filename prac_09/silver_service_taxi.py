from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """"""
    flagfall = 4.50

    def __init__(self, kwargs, fanciness):
        """Initialize name, fuel, fanciness"""
        super().__init__(**kwargs)
        self.fanciness = float(fanciness)
        #set price_per_km
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus falgfall of ${self.flagfall}"

