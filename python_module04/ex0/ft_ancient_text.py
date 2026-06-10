#!/usr/bin/env python3

import sys
from typing import TextIO


def main() -> None:
    pro_name, *files_name = sys.argv
    pro_name = pro_name.split("/")[-1]
    if len(files_name) == 0:
        print(f"Usage: {pro_name} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    for arg in files_name:
        print(f"Accessing file '{arg}'")
        try:
            f: TextIO = open(arg, "r")
            try:
                content: str = f.read()
                print("---\n")
                print(content, end="")
                print("\n---")
            finally:
                f.close()
                print(f"File '{arg}' closed.")
        except OSError as e:
            print(f"Error opening file '{arg}': {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
