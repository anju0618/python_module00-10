#!/usr/bin/env python3
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return 'Spell fizzled'
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_caster(target: str, power: int) -> list[str]:
        result = []
        for spell in spells:
            spell_res = spell(target, power)
            result.append(spell_res)
        return result
    return sequence_caster


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def high_power_condition(target: str, power: int) -> bool:
        return power >= 50

    print("--- 1. Testing spell combiner ---")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 50))

    print("\n--- 2. Testing power amplifier ---")
    amplified = power_amplifier(fireball, 3)
    print(amplified("Orc", 10))

    print("\n--- 3. Testing conditional caster ---")
    caster = conditional_caster(high_power_condition, fireball)
    print("Power 60:", caster("Goblin", 60))
    print("Power 30:", caster("Goblin", 30))

    print("\n--- 4. Testing spell sequence ---")
    sequence = spell_sequence([fireball, heal, fireball])
    print(sequence("Slime", 20))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
