from typing import Callable
from engine.ship import Ship


def is_one_approaching(last: float, current: float, is_hitted: dict[str, bool]):
    """Коооостылььь"""
    is_hitted['value'] = not is_hitted['value']
    return current <= last and is_hitted['value']

def create_attack_checker(ship1: Ship, ship2: Ship):
    max_attack_distance = max(ship1.attack_range, ship2.attack_range)
    first_distance = ship1.get_distance_between(ship2)

    is_hitted = { "value": False }

    def can_any_attack() -> bool:
        current_distance = ship1.get_distance_between(ship2)
        return current_distance <= max_attack_distance or is_one_approaching(first_distance, current_distance, is_hitted)

    return can_any_attack


def is_both_alive(ship1: Ship, ship2: Ship) -> bool:
    return ship1.is_alive() and ship2.is_alive()


async def calculate_moves(ship1: Ship, ship2: Ship, printer: Callable[[str], None]):
    ship1.set_result_printer(printer)
    ship2.set_result_printer(printer)

    can_any_attack = create_attack_checker(ship1, ship2)

    """
    Пока корабли сближаются или один из них или оба могут атаковать
    """

    while can_any_attack():
        printer(f'Distence between {ship1.name} and {ship2.name} is {ship1.get_distance_between(ship2): .02f}')

        ship1.attack(ship2)
        ship2.attack(ship1)

        printer()

        if not is_both_alive(ship1, ship2):
            break

        ship1.change_coords()
        ship2.change_coords()
