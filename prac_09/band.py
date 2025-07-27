class Band():
    """It represents a band consisting of multiple musicians.

    This class is used to manage the musicians in the band and provides methods for each musician in the band to play their instrument."""
    def __innit__(self, name):
        """Initialise the band name and musicians list"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musicians to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return the string representation of the band"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Play the instrument"""
        result = []
        for musician in self.musicians:
            result.append(musician.play()) #Call the play method of each musician and add the result to the list
        return "\n".join(result)


