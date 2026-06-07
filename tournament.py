#!/usr/bin/env python3
from typing import List, Tuple
from ex0 import AquaFactory, FlameFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyException,
    NormalStrategy,
)
from ex2.strategy import BattleStrategy


def run_tournament(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            try:
                log1 = strategy1.act(c1)
                log2 = strategy2.act(c2)

                print(log1)
                print(log2)

            except InvalidStrategyException as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    normal_s = NormalStrategy()
    defensive_s = DefensiveStrategy()
    aggressive_s = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive)]")
    opponents_basic = [(flame_f, normal_s), (heal_f, defensive_s)]
    run_tournament(opponents_basic)
    print()

    print("Tournament 1 (error)")
    print(" [(Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_error = [(flame_f, aggressive_s), (heal_f, defensive_s)]
    run_tournament(opponents_error)
    print()

    print("Tournament 2 (multiple)")
    print(" [(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    opponents_multi = [
        (aqua_f, normal_s),
        (heal_f, defensive_s),
        (trans_f, aggressive_s),
    ]
    run_tournament(opponents_multi)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
