"""
estimate time: 40min
actual time:
"""
class Project:
    """Storing project information and providing auxiliary methods"""
    def __init__(self, name, start_date, priority:int, cost_estimate:float, completion_percentage:int):
        """Initialize Project class"""
        self.name = name
        self.start_date = start_date  # datetime.date对象
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Support sorting by priority"""
        return self.priority < other.priority

    def is_completed(self):
        """Determine whether the project has been completed"""
        return self.completion_percentage == 100

    def __str__(self):
        """Return string"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

