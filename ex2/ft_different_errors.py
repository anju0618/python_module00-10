#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        _ = "str" + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(4):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")

    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operatuib completed successfully")
    except Exception as e:
        print(f"Caught unexpected error: {e}")

    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        pass

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
