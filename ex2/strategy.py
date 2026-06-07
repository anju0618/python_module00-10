#!/usr/bin/env python3

import abc
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        if isinstance(creature, TransformCapability):
            log1 = creature.transform()
            log2 = creature.attack()
            log3 = creature.revert()
            return f"{log1}\n{log2}\n{log3}"
        return ""


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        if isinstance(creature, HealCapability):
            log1 = creature.attack()
            log2 = creature.heal()
            return f"{log1}\n{log2}"
        return ""
