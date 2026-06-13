#!/usr/bin/env python3
import functools
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    op_map = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda x, y: max(x, y),
        "min": lambda x, y: min(x, y),
        }

    if operation not in op_map:
        raise ValueError(f"Unknown operation: {operation}")

    func = op_map[operation]
    return functools.reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, 50, "Fire")
    ice = functools.partial(base_enchantment, 50, "Ice")
    lightning = functools.partial(base_enchantment, 50, "Lightning")
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return spell

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]

    print(f"\nSum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Empty: {spell_reducer([], 'add')}")

    print("\nTesting partial enchanter...")

    def raw_enchant(power: int, element: str, target: str) -> str:
        return f"{element} Enchantment (Power: {power}) applied to {target}"
    enchanters = partial_enchanter(raw_enchant)
    print(enchanters["fire_enchant"]("Sword"))
    print(enchanters["ice_enchant"]("Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(50): {memoized_fibonacci(50)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(f"Unknown type: {dispatcher(3.14)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
