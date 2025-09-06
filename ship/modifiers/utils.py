from enum import IntEnum
from typing import Protocol


class ShipInterface(Protocol):
    name: str
    ship_type: str
    nation: str
    damage: float
    attack_range: float
    hp: float
    velocity: float


class ModifiersPriority(IntEnum):
    BY_SHIP = 1
    BY_TYPE = 2
    BY_NATION = 3


class ModifierFn(Protocol):
    def __call__(self, distance: float, damage: float, attacker: ShipInterface, attacked: ShipInterface) -> float: ...


class Modifier:
    slots = ['priority', 'modifier', '__repr__']

    def __init__(self, modifier: ModifierFn, priority: ModifiersPriority):
        self.modifier = modifier
        self.priority = priority

    def __repr__(self):
        return f'Modifier(modifier={self.modifier.__name__}, priority={self.priority})'


class ModifiersOption:
    slots = ['priority', 'items']

    def __init__(self, priority: ModifiersPriority, items: list[ModifierFn] | None = None):
        self.priority = priority
        self.items = items or []


def register_modifier(a_register: ModifiersOption):
    def wrapper(modifier: ModifierFn):
        a_register.items.append(modifier)
        return modifier

    return wrapper
