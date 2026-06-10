#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    raw_name, *score_args = sys.argv
    prog_name = raw_name.split("/")[-1]
    valid_scores = []
    for arg in score_args:
        try:
            num = int(arg)
            valid_scores.append(num)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(valid_scores) == 0:
        print(f"No scores provided. Usage: python3 "
              f"{prog_name} <score1> <score2> ...")
        return

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len(valid_scores)}")
    print(f"Total score: {sum(valid_scores)}")
    print(f"Average score: {sum(valid_scores) / len(valid_scores)}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")


if __name__ == "__main__":
    main()
