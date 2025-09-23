from engine.calculate_moves import calculate_moves
from engine.ship import Ship


def start_battle(ship1: Ship, ship2: Ship):
    calculate_moves(ship1, ship2)

    print()
    """
    Использовал логическую эквивалентность (A <--> B), так как логическая эквивалентность истинна тогда и только тогда,
    когда оба операнда имеют одинаковое логическое значение (оба истинны или оба ложны).
    Если оба истина то корабли живы или если оба ложны то уничтожены
    """
    if not (ship1.is_alive() ^ ship2.is_alive()):
        return('Ничья')
    elif ship1.is_alive():
        return('Победа I')
    else:
        return('Победа II')
