import asyncio
from engine.calculate_moves import calculate_moves
from engine.existing_ships import input_validated_ship

async def main():
    ship_1 = input_validated_ship("Enter first ship name: ")
    ship_2 = input_validated_ship("Enter second ship name: ")
    print()

    await calculate_moves(ship_1, ship_2, print)

    print()
    """
    Использовал логическую эквивалентность (A <--> B), так как логическая эквивалентность истинна тогда и только тогда, 
    когда оба операнда имеют одинаковое логическое значение (оба истинны или оба ложны).
    Если оба истина то корабли живы или если оба ложны то уничтожены
    """
    if not (ship_1.is_alive() ^ ship_2.is_alive()):
        print('Ничья')
    elif ship_1.is_alive():
        print('Победа I')
    else:
        print('Победа II')

if __name__ == "__main__":
    asyncio.run(main())