#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
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

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


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
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
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
        self.set_age(self.get_age() + 1)
        self.nutritional_value += 5

    def grow(self):
        self.set_height(self.get_height() + 2.0)
        self.nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("\n[asking the rose to bloom]")
    rose.bloom()

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("\n[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("\n[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
