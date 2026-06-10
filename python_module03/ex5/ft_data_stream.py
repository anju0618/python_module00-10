#!/usr/bin/env python3

import typing
import random

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while 1:
        p = random.choice(PLAYERS)
        a = random.choice(ACTIONS)
        yield (p, a)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        picked = random.choice(event_list)
        event_list.remove(picked)
        yield picked


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()
    for i in range(1000):
        player, action = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = [next(event_stream) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    consumer = consume_event(ten_events)

    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
