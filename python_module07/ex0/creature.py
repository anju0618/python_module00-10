#!/usr/bin/env python3

import abc
import typing


class Creature(abc.ABC):
    def __init__(
        self, name: str, element_type: typing.Union[str, typing.List[str]]
    ) -> None:
        self.name = name
        self.element_type = element_type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        if isinstance(self.element_type, list):
            type_str = "/".join(self.element_type)
        else:
            type_str = self.element_type

        return f"{self.name} is a {type_str} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", element_type="Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", element_type=["Fire", "Flying"])

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", element_type="Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", element_type="Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"


def main() -> None:
    creatures = [Flameling(), Pyrodon(), Aquabub(), Torragon()]
    print("--- Testing describe & attack ---")
    for c in creatures:
        print(c.describe())
        print(c.attack())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
