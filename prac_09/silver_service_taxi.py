from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """The class representing SilverServiceTaxi inherits from the Taxi class.

    This type is used to simulate silver service taxis, featuring an additional starting fare and per-kilometer price adjustments based on fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize name, fuel, fanciness"""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        #set price_per_km
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return the string representation of SilverServiceTaxi."""
        return f"{super().__str__()} plus falgfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the silver taxi trip."""
        return super().get_fare() + self.flagfall



