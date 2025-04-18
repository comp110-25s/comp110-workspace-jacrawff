"""File to define River class."""

__author__ = "730649503"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Defining River."""

    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking ages of bear and fish."""
        surv_fish: list = []
        surv_bears: list = []
        for fish in self.fish:
            if fish.age <= 3:
                surv_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surv_bears.append(bear)
        self.fish = surv_fish
        self.bears = surv_bears
        return None

    def bears_eating(self):
        """Modeling bears eating behavior."""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(amount=3)
                bear.eat(num_fish=3)
        return None

    def check_hunger(self):
        """Checking hunger levels."""
        checked_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                checked_bears.append(bear)
        self.bears = checked_bears
        return None

    def repopulate_fish(self):
        """Fish growth in river."""
        num_new_fish = (len(self.fish) // 2) * 4
        while num_new_fish > 0:
            new_fish = Fish()
            self.fish.append(new_fish)
            num_new_fish -= 1
        return None

    def repopulate_bears(self):
        """Bear growth in river."""
        num_new_bears = len(self.bears) // 2
        while num_new_bears > 0:
            new_bear = Bear()
            self.bears.append(new_bear)
            num_new_bears -= 1
        return None

    def view_river(self):
        """Viewing river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Modeling one week for a river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Taking fish out of river."""
        idx: int = 0
        while idx < amount and self.fish:
            self.fish.pop(0)
            idx += 1
