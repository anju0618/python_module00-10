#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def grow(self, increase: float) -> None:
        self.height += increase

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age = 30

    start_height = rose.height
    rose.show()

    for i in range(1, 8):
        print(f"===Day {i}===")
        rose.grow(0.8)
        rose.age_one_day()
        rose.show()

    total_growth = rose.height - start_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
