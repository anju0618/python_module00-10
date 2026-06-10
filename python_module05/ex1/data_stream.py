#!/usr/bin/env python3

from __future__ import annotations
import typing
import abc


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            found = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    found = True
                    break
            if not found:
                print(f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = proc.get_total_processed()
            remaining = proc.get_remaining_count()
            print(f"{name}: total {total} items processed,"
                  f" remaining {remaining} on processor")


"""
ex0の部品>>>
"""


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

    # add def
    def get_total_processed(self) -> int:
        return self._rank_counter

    def get_remaining_count(self) -> int:
        return len(self._storage)


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


"""
ex0の部品<<<
"""


def main() -> None:
    print("=== Code Nexus Data Stream ===")

    print("\nInitialize Data Stream..")
    stream_sys = DataStream()
    stream_sys.print_processors_stats()

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("\nRegistering Numeric Processor")
    stream_sys.register_processor(num_proc)

    batch = [
        'Hello world',
        [3.14, 1, -2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    print("\nSend first batch of data on stream:")
    stream_sys.process_stream(batch)
    stream_sys.print_processors_stats()

    print("\nRegistering other data processors")
    stream_sys.register_processor(text_proc)
    stream_sys.register_processor(log_proc)

    print("Send the same batch again")
    stream_sys.process_stream(batch)
    stream_sys.print_processors_stats()

    print("\nConsume some elements from the"
          "data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream_sys.print_processors_stats()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
