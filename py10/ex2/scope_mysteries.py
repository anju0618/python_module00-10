#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    accumulate_pow = initial_power

    def accumulate(power: int) -> int:
        nonlocal accumulate_pow
        accumulate_pow += power
        return accumulate_pow
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_item(item_name: str) -> str:
        res = f"{enchantment_type} {item_name}"
        return res
    return enchant_item


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")

    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    store_func = vault["store"]
    recall_func = vault["recall"]

    print("Store 'secret' = 42")
    store_func("secret", 42)

    print(f"Recall 'secret': {recall_func('secret')}")
    print(f"Recall 'unknown': {recall_func('unknown')}")


if __name__ == "__main__":
    main()
