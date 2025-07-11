"""
Estimate time: 20min
Actual time: 20min
"""
class Guitar:
    """A class representing guitars, used to store the name, production year and cost of the guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Initialize the Guitar object and set the name, production year and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation containing the guitar name, production year and cost."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate and return the age of the guitar (based on 2025)."""
        return 2025-self.year

    def is_vintage(self):
        """To determine if a guitar is a vintage one (if it is 50 years old or older, it is considered vintage)"""
        return self.get_age() >= 50

    main()