import asyncio
from typing import Any, Callable, Coroutine

from engine.calculate_moves import calculate_moves
from engine.ship import Ship


EOF = '!game_end!'


def create_battle(ship1: Ship, ship2: Ship) -> tuple[asyncio.Queue[str], Coroutine[None, None, None], str]:
    messages = asyncio.Queue()

    def print_producer(msg: str="", end: str="\n"):
        messages.put_nowait(msg)
        messages.put_nowait(end)

    async def start_battle_wrapper():
        await start_battle(ship1, ship2, print_producer)

    return messages, start_battle_wrapper, EOF


async def start_battle(ship1: Ship, ship2: Ship, printer: Callable[[str], Any]):

    await calculate_moves(ship1, ship2, printer)

    printer()

    """
    Использовал логическую эквивалентность (A <--> B), так как логическая эквивалентность истинна тогда и только тогда,
    когда оба операнда имеют одинаковое логическое значение (оба истинны или оба ложны).
    Если оба истина то корабли живы или если оба ложны то уничтожены
    """

    if not (ship1.is_alive() ^ ship2.is_alive()):
        printer('Ничья')
    elif ship1.is_alive():
        printer(f'Победа {ship1.name}')
    else:
        printer(f'Победа {ship2.name}')

    printer(EOF)