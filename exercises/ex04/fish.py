"""File to define Fish class."""

__author__ = "730649503"


class Fish:
    """Defining fish."""

    age: int

    def __init__(self):
        """Initializing fish."""
        self.age = 0
        return None

    def one_day(self):
        """What happens to fish after one day."""
        self.age += 1
        return None
