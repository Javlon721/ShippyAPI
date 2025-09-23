import asyncio
from typing import Any, Callable
from engine.calculate_moves import calculate_moves
from engine.ship import Ship


EOF = '!game_end!'


async def start_battle(ship1: Ship, ship2: Ship, printer: asyncio.Queue[str]):

    def print_producer(msg: str="", end: str="\n"):
        printer.put_nowait(msg)
        printer.put_nowait(end)

    await calculate_moves(ship1, ship2, print_producer)

    print_producer()

    """
    Использовал логическую эквивалентность (A <--> B), так как логическая эквивалентность истинна тогда и только тогда,
    когда оба операнда имеют одинаковое логическое значение (оба истинны или оба ложны).
    Если оба истина то корабли живы или если оба ложны то уничтожены
    """

    if not (ship1.is_alive() ^ ship2.is_alive()):
        print_producer('Ничья')
    elif ship1.is_alive():
        print_producer('Победа I')
    else:
        print_producer('Победа II')

    print_producer(EOF)