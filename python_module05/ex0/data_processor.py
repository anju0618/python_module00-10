#!/usr/bin/env python3

import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            return (-1, "")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self._storage.append((self._rank_counter, str(data)))
            self._rank_counter += 1
        elif isinstance(data, list):
            for x in data:
                self._storage.append((self._rank_counter, str(x)))
                self._rank_counter += 1


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._storage.append((self._rank_counter, data))
            self._rank_counter += 1
        elif isinstance(data, list):
            for x in data:
                self._storage.append((self._rank_counter, x))
                self._rank_counter += 1


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items())
        if isinstance(data, list):
            if not data:
                return False
            return all(
                isinstance(x, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in x.items()
                )
                for x in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]):
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            log_str = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._rank_counter, log_str))
            self._rank_counter += 1
        elif isinstance(data, list):
            for x in data:
                log_str = f"{x['log_level']}: {x['log_message']}"
                self._storage.append((self._rank_counter, log_str))
                self._rank_counter += 1


def main() -> None:
    print("=== Code Nexus Data Processor ===")

    print("\nTesting Numeric Processor.")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # type:ignore
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num_proc.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {i}: ", end="")
        print(val)

    print("\nTesting Text Processor.")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_proc.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value 0: {val}")

    print("\nTesting Log Processor.")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!!'}
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {i}: {val}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
