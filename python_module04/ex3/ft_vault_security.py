#!/usr/bin/env python3

import typing
import sys


def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> typing.Tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as f:
                data: str = f.read()
            return (True, data)
        elif action == "write":
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: '{action}'. "
                           f"Use 'read' or 'write'.")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read:")
    print(secure_archive("ancient_fragment.txt", "read"))

    print("Using 'secure_archive' to write:")
    print(secure_archive("secure_vault.txt", "write", "System Online 2087\n"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
