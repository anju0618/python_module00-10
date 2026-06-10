#!/usr/bin/env python3

from __future__ import annotations
import typing
import abc


class ExportPlugin(typing.Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        if not data:
            return
        parts = [x[1] for x in data]
        print(", ".join(parts))


class JSONPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        if not data:
            return
        json_elements = []
        for rank, val in data:
            json_elements.append(f'"item_{rank}": "{val}"')
        json_str = "{" + ", ".join(json_elements) + "}"
        print(json_str)


"""
from ex1
"""


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
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total = proc.get_total_processed()
            remaining = proc.get_remaining_count()
            print(f"{name}: total {total} items processed,"
                  f" remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            exported_data: list[tuple[int, str]] = []
            for _ in range(nb):
                rank, val = proc.output()
                if rank == -1:
                    break
                exported_data.append((rank, val))
            if exported_data:
                plugin.process_output(exported_data)


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
end of ex1
"""


def main() -> None:
    print("=== Code Nexus Data Pipeline ===")

    print("\nInitialize Data Stream")
    stream_sys = DataStream()
    stream_sys.print_processors_stats()

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("\nRegistering Processors")
    stream_sys.register_processor(num_proc)
    stream_sys.register_processor(text_proc)
    stream_sys.register_processor(log_proc)

    batch1 = [
        'Hello world',
        [3.14, 1, -2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': (
                    'Telnet access! '
                    'Use ssh instead'
                )
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
    stream_sys.process_stream(batch1)
    stream_sys.print_processors_stats()

    # CSVTEST
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    stream_sys.output_pipeline(3, csv_plugin)
    stream_sys.print_processors_stats()

    # bench2
    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("\nSend another batch of data:")
    stream_sys.process_stream(batch2)
    stream_sys.print_processors_stats()

    # JSONTEST
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    stream_sys.output_pipeline(5, json_plugin)
    stream_sys.print_processors_stats()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
