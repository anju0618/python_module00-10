#!/usr/bin/env python3

import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            return (-1, "")
        data_str: str = self._storage.pop(0)



class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool
        if isinstance(data, (int, float))

    def ingest

class TextProcessor(DataProcessor):


class LogProcessor(DataProcessor):




if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
