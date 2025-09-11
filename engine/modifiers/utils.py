from enum import IntEnum
from typing import Protocol, Any, Callable


class ShipInterface(Protocol):
    name: str | None = None
    ship_type: str | None = None
    nation: str | None = None
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
        self.name = modifier.__name__

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


def bin_search(l: int, r: int, arr: list[Any], target: Any, check: Callable[[Any, Any], bool]):
    while l < r:
        m = (l + r) // 2
        if check(arr[m], target):
            r = m
        else:
            l = m + 1
    return l
