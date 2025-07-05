"""
Estimate time: 20min
Actual time: 30min
"""
from docutils.nodes import reference

class ProgrammingLanguage:
    """ """
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year} "

