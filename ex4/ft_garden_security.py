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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    print("\nNormal Test")
    rose = Plant("Rose", 15.0, 10)
    rose.show()

    print("\nNegative Test")
    negative = Plant("Neg", -10.0, -5)
    negative.show()

    print("\nSetter Test")
    rose.set_height(-40.0)
    rose.show()
