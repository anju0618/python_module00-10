#!/usr/bin/env python3

import sys
from typing import TextIO


def ft_ancient_text(arg: str) -> str:
    print(f"Accessing file '{arg}'")
    try:
        f: TextIO = open(arg, "r")
        try:
            content: str = f.read()
            print("---\n")
            print(content, end="")
            print("\n---")
            return content
        finally:
            f.close()
            print(f"File '{arg}' closed.")
    except OSError as e:
        print(f"Error opening file '{arg}': {e}", file=sys.stderr)
        raise e


def ft_archive_creation(content: str) -> None:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = []
    print("Transform data:")
    print("---")
    for line in lines:
        new_line: str = line + '#'
        print(new_line)
        transformed_lines.append(new_line)
    print("---")

    final_content: str = "\n".join(transformed_lines) + "\n"
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    save_name: str = sys.stdin.readline().rstrip("\n")

    if save_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{save_name}'")
    try:
        out_f: TextIO = open(save_name, "w")
        try:
            out_f.write(final_content)
            print("Data saved in file '{save_name}'")
        finally:
            out_f.close()
    except OSError as e:
        print(f"Error saving file '{save_name}': {e}", file=sys.stderr)
        print("Data not saved.")


def main() -> None:
    pro_name, *files_name = sys.argv
    pro_name = pro_name.split("/")[-1]

    if len(files_name) == 0:
        print(f"Usage: {pro_name} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    for arg in files_name:
        try:
            content: str = ft_ancient_text(arg)
            ft_archive_creation(content)
        except OSError:
            continue


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
