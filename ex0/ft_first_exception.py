#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("Input data is '25'")
    try:
        test1 = input_temperature("25")
        print(f"Temperature is now {test1}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is 'abc'")
    try:
        _ = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
