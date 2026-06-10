#!/usr/bin/env python3

import sys
import os
import site


def is_virtual() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if not is_virtual():
        print("\nMATRIX STATUS: You're still plugged in")

        current_python = sys.executable
        print(f"\nCurrent Python: {current_python}")
        print("Virtual Environment: None detected")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")

    else:
        print("\nMATRIX STATUS: Welcome to the construct")

        current_python = sys.executable
        env_path = sys.prefix
        env_name = os.path.basename(sys.prefix)
        print(f"\nCurrent Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        package_path = site.getsitepackages()[0]
        print("\nPackage installation path:")
        print(f"{package_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
