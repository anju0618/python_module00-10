#!/usr/bin/env python3
from collections.abc import Callable
import functools
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None and args:
                if len(args) == 1:
                    power = args[0]
                elif len(args) == 3:
                    power = args[2]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"
    result = fireball()
    print(f"Result: {result}")
    print()

    @power_validator(min_power=50)
    def charge_beam(power: int) -> str:
        return f"Beam fired with {power} power!"

    print(charge_beam(60))
    print(charge_beam(30))
    print(charge_beam(55))
    print()

    print("Testing retrying spell")
    fail_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        nonlocal fail_count
        if fail_count < 2:
            fail_count += 1
            raise RuntimeError("Mana fluctuation")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())
    print()

    @retry_spell(max_attempts=3)
    def broken_spell() -> str:
        raise RuntimeError("Complete fizzle")

    print(broken_spell())
    print()

    print("Testing MageGuild...")
    guild = MageGuild()

    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Al"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
