#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def main() -> None:
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()

    print(" base:")
    base_heal = heal_factory.create_base()
    print(base_heal.describe())
    print(base_heal.attack())
    if isinstance(base_heal, HealCapability):
        print(base_heal.heal())

    print(" evolved:")
    evolved_heal = heal_factory.create_evolved()
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    if isinstance(evolved_heal, HealCapability):
        print(evolved_heal.heal())

    print("\nTesting Creature with transform capability")
    trans_factory = TransformCreatureFactory()

    print(" base:")
    base_trans = trans_factory.create_base()
    print(base_trans.describe())
    print(base_trans.attack())
    if isinstance(base_trans, TransformCapability):
        print(base_trans.transform())
        print(base_trans.attack())
        print(base_trans.revert())

    print(" evolved:")
    evolved_trans = trans_factory.create_evolved()
    print(evolved_trans.describe())
    print(evolved_trans.attack())
    if isinstance(evolved_trans, TransformCapability):
        print(evolved_trans.transform())
        print(evolved_trans.attack())
        print(evolved_trans.revert())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
