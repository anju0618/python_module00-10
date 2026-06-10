#!/usr/bin/env python3
import sys


def print_program_name() -> None:
    pro_name = sys.argv[0].split("/")[-1]
    print(f"Program name: {pro_name}")


def print_arg_count() -> None:
    ac = len(sys.argv) - 1
    if ac >= 1:
        print(f"Arguments received: {ac}")
    elif ac == 0:
        print("No arguments provided!")
    return


def print_arg_name() -> None:
    """
    pure_args = sye.argv[1:]
    for i, arg in enumerate(pure_args, start=1):
        print(f"Argument {i}: {arg}")
    return
    prog_name, *pure_args = sys.argv

    for i, arg in enumerate(pure_args, start=1):
        print(f"Argument {i}: {arg}")
    return
    """
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
    return


def print_total_arg() -> None:
    ac = len(sys.argv)
    print(f"Total arguments: {ac}")


def main() -> None:
    print("=== Command Quest ===")
    print_program_name()
    print_arg_count()
    print_arg_name()
    print_total_arg()
    return


if __name__ == "__main__":
    main()
