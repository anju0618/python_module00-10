#!/usr/bin/env python3

import random as rd

AC_POOL = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps", "Sharp Mind"
    ]


def gen_player_achievements() -> set[str]:
    count = rd.randint(5, 9)
    picked = rd.sample(AC_POOL, count)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = set.union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")

    common_ac = set.intersection(alice, bob, charlie, dylan)
    print(f"\nCommon achievements: {common_ac}")

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)
    print(f"\nOnly Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    ma = all_distinct.difference(alice)
    mb = all_distinct.difference(bob)
    mc = all_distinct.difference(charlie)
    md = all_distinct.difference(dylan)

    print(f"\nAlice is missing: {ma}")
    print(f"Bob is missing: {mb}")
    print(f"Charlie is missing: {mc}")
    print(f"Dylan is missing: {md}")
    return


"""
def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name, ac_set in players.items():
        print(f"Player {name}: {ac_set}")

    all_distinct = set.union(*players.values())
    common_ac = set.intersection(*players.values())

    print(f"\nAll distinct achievements: {all_distinct}")
    print(f"Common achievements: {common_ac}\n")

    for name, ac_set in players.items():
        others = set.union(
            *(p_set for p_name, p_set in players.items() if p_name != name)
            )
        only_this_player = ac_set.difference(others)
        missing_ac = all_distinct.difference(ac_set)
        print(f"Only {name} has: {only_this_player}")
        print(f"{name} is missing: {missing_ac}")
"""


if __name__ == "__main__":
    main()
