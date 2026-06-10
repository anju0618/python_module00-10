#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self._stats = self.Stats()
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return
        self._height = new_height

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return
        self._age = new_age

    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self):
            self._grow_calls += 1

        def record_age(self):
            self._age_calls += 1

        def record_show(self):
            self._show_calls += 1

        def get_grow_calls(self):
            return self._grow_calls

        def get_age_calls(self):
            return self._age_calls

        def get_show_calls(self):
            return self._show_calls

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.record_show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, colour: str):
        super().__init__(name, height, age)
        self.colour = colour

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Colour: {self.colour}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def record_shade(self):
            self._shade_calls += 1

        def get_shade_calls(self):
            return self._shade_calls

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.Stats()

    def produce_shade(self):
        self._stats.record_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{self.get_height()}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self):
        self._stats.record_age()
        self.set_age(self.get_age() + 1)
        self.nutritional_value += 5

    def grow(self):
        self._stats.record_grow()
        self.set_height(self.get_height() + 2.0)
        self.nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, colour: str):
        super().__init__(name, height, age, colour)
        self.seed_count = 0
        self.bloom_flag = False

    def bloom(self) -> None:
        super().bloom()
        self.seed_count += 42
        self.bloom_flag = True

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")

    grow_c = plant._stats.get_grow_calls()
    age_c = plant._stats.get_age_calls()
    show_c = plant._stats.get_show_calls()

    print(f"Stats: {grow_c} grow, {age_c} age, {show_c} show")
    if isinstance(plant, Tree):
        assert isinstance(plant._stats, Tree.Stats)
        shade_c = plant._stats.get_shade_calls()
        print(f"Additional stats: {shade_c} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("\n=== Check year-old ===")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")

    print("\n=== Anonymous ===")
    anon = Plant.create_anonymous()
    anon.show()

    print("\n=== Statistics Check ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    for _ in range(3):
        tomato.grow()
        tomato.age()
    tomato.show()
    display_statistics(tomato)
    print("\n")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.produce_shade()
    oak.show()
    display_statistics(oak)
