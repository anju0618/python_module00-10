#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z'")
        start_list = user_input.split(",")
        if len(start_list) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(start_list[0])
            y = float(start_list[1])
            z = float(start_list[2])
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter ... {e}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x = pos1[0]
    y = pos1[1]
    z = pos1[2]
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to centre: {math.sqrt((x * x) + (y * y) + (z * z)):.4f}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    x2 = pos2[0]
    y2 = pos2[1]
    z2 = pos2[2]
    print(f"Distance between the 2 sets of coordinates:"
          f" {math.sqrt((x - x2)**2 + (y - y2)**2 + (z - z2)**2):.4f}")


if __name__ == "__main__":
    main()
