#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f" * {x} * ", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_pow = max(mages, key=lambda x: x['power'])
    min_pow = min(mages, key=lambda x: x['power'])
    avg_value = sum(items['power'] for items in mages) / len(mages)
    avg_pow = round(avg_value, 2)
    return {
        "max_power": max_pow['power'],
        "min_power": min_pow['power'],
        "avg_power": avg_pow
        }


def main() -> None:
    print("Testing artifact sorter...")
    test_artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Orb"},
        {"name": "Fire Staff", "power": 92, "type": "Staff"},
        {"name": "Iron Sword", "power": 40, "type": "Sword"},
    ]
    sorted_artifacts = artifact_sorter(test_artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")
    print("\nTesting power filter...")
    test_mages = [
        {"name": "Alex", "power": 95, "element": "Fire"},
        {"name": "Jordan", "power": 70, "element": "Water"},
        {"name": "Riley", "power": 82, "element": "Earth"}
    ]
    filtered_mages = power_filter(test_mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in filtered_mages]}")
    print("\nTesting spell transformer...")
    test_spells = ["fireball", "heal", "shield"]
    transformed_spells = spell_transformer(test_spells)
    for spell in transformed_spells:
        print(spell.strip())

    print("\nTesting mage stats...")
    stats = mage_stats(test_mages)
    print(f"Stats: {stats}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
