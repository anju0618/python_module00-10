#!/usr/bin/env python3

import sys


def deal_args() -> dict[str, int]:
    inventory = {}
    prog_name, *pure_args = sys.argv
    for arg in pure_args:
        if ":" not in arg:
            print(f"Error invalid parameter '{arg}'")
            continue
        item_name, quantity_str = arg.split(":", 1)
        if item_name in inventory:
            print(f"Redundant item '{item_name}' discarding")
            continue
        try:
            quantity_int = int(quantity_str)
            inventory[item_name] = quantity_int
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
    return (inventory)


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = deal_args()
    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for arg in inventory:
        rep = (inventory[arg] / total_qty) * 100
        print(f"Item {arg} represents {rep:.1f}%")

    most_item = max(inventory, key=lambda k: inventory[k])
    least_item = min(inventory, key=lambda k: inventory[k])
    print(f"Item most abundant: {most_item} "
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} "
          f"with quantity {inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
