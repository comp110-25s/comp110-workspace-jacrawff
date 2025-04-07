"""File to define Bear class."""

__author__ = "730649503"


class Bear:
    """Defiining Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing Bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Changing variables after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """What happens to bear after eating."""
        self.hunger_score += num_fish
