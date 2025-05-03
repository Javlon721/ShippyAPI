from existing_ships import get_ship_by_name
from ship import Ship, calculate_moves, get_random_positions
from game_errors import ShipNameNotFound


# while True:
#     try:
#         ship_1 = get_ship_by_name(input("Enter first ship name: "))
#         break
#     except ShipNameNotFound as e:
#         print(e)
# while True:
#     try:
#         ship_2 = get_ship_by_name(input("Enter second ship name: "))
#         break
#     except ShipNameNotFound as e:
#         print(e)
# while True:
#     distance_between_ships = input("Enter distance between ships (km): ")
#     if distance_between_ships.isdigit():
#         distance_between_ships = float(distance_between_ships)
#         break
#     print('Enter valid number')
# while True:
#     ships_direction = input("Enter ships direction (0, 1, 2 or 3): ")
#     match ships_direction:
#         case '0' | "1" | "2" | "3":
#             break
#         case _:
#             print('Enter valid number (0, 1, 2 or 3)')


ship_1 = get_ship_by_name('Hipper')
ship_2 = get_ship_by_name('Belfast')
ships_direction = input("Enter ships direction (0, 1, 2 or 3): ")
distance_between_ships = int(input("Enter distance between ships (km): "))

rand_pos1, rand_pos2 = get_random_positions(distance_between_ships) 
ship_1.set_pos(rand_pos1)
ship_2.set_pos(rand_pos2)

#* Нужно поменять направление погони относительно где стоит ship_2.
#* Например если ship_2 догоняет ship_1 и если позиция ship_2 правее чем ship_1 
#* то их позиции уменьшаются (<- ship_1 <- ship_2) и наоборот (ship_2 -> ship_1 ->)
if ship_2.pos < ship_1.pos:
    direction_map = {
        '2': '3',
        '3': '2'
    }
    ships_direction = direction_map.get(ships_direction, ships_direction)
    calculate_moves(ship_2, ship_1, ships_direction)
else:
    calculate_moves(ship_1, ship_2, ships_direction)

print('-' * 30)
Ship.print_ships(ship_1, ship_2)