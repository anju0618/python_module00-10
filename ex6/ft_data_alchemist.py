#!/usr/bin/env python3

import random

ip = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
    ]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"\nInitial list of players: {ip}")

    all_cp = [name.capitalize() for name in ip]
    print(f"New list with all names capitalized: {all_cp}")

    only_cp = [name for name in ip if name and name[0].isupper()]
    print(f"New list of capitalized name only: {only_cp}")

    score_dict = {name: random.randint(1, 1000) for name in all_cp}
    print(f"Score dict: {score_dict}")

    avg_score = sum(score_dict.values()) / len(score_dict)
    high_scores = {
        name: score for name, score in score_dict.items() if score > avg_score
        }
    print(f"Score average is {avg_score:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
