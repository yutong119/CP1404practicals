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


