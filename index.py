from existing_ships import get_ship_by_name, input_validated_ship
from ship import Ship, calculate_moves, set_ship_position
from game_errors import ShipNameNotFound

ship_1 = input_validated_ship("Enter first ship name: ")
set_ship_position(ship_1)
ship_2 = input_validated_ship("Enter second ship name: ")
set_ship_position(ship_2)
print()

calculate_moves(ship_1, ship_2)

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
