#!/usr/bin/env python3

from ex0 import AquaFactory, FlameFactory
from ex0.factory import CreatureFactory


def verify_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle_base(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")

    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    verify_factory(flame_factory)
    print()
    verify_factory(aqua_factory)
    print()

    battle_base(flame_factory, aqua_factory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
