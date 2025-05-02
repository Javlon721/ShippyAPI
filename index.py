from existing_ships import get_ship_by_name
from ship import Ship
from game_errors import ShipNameNotFound
from random import randint

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

ship_2 = get_ship_by_name('Belfast')
ship_1 = get_ship_by_name('Bismarck')
ships_direction = input("Enter ships direction (0, 1, 2 or 3): ")
distance_between_ships = int(input("Enter distance between ships (km): "))
ship1_new_pos = randint(0, 100)
ship2_new_pos = ship1_new_pos + distance_between_ships
ship_1.set_pos(ship1_new_pos)
ship_2.set_pos(ship2_new_pos)
max_distance_between_ships = max(ship_1.attack_range, ship_2.attack_range)

print("=" * 30)
print(f'{ship_1.name} attack distance: {ship_1.attack_range} | {ship_2.name}  attack distance: {ship_2.attack_range}')
print(f'{ship_1.name} velocity:  {ship_1.velocity} | {ship_2.name}  velocity: {ship_2.velocity}')
print("=" * 30)

match ships_direction:
    case '0':
        while ship_2.pos - ship_1.pos > 0 or ship_1.pos - ship_2.pos <= max_distance_between_ships:
            print("=" * 30)
            ship_1.change_pos()
            ship_2.change_pos(-1)
            print(
                f'{ship_1.name} pos: {ship_1.pos} | {ship_2.name} pos: {ship_2.pos}')
            print("-" * 30)
            print(f'current distance: {ship_2.pos - ship_1.pos: .2f}')
    case '1':
        while ship_2.pos - ship_1.pos <= max_distance_between_ships:
            print("=" * 30)
            ship_1.change_pos(-1)
            ship_2.change_pos()
            print(
                f'{ship_1.name} pos: {ship_1.pos} | {ship_2.name} pos: {ship_2.pos}')
            print("-" * 30)
            print(f'current distance: {ship_2.pos - ship_1.pos: .2f}')
    case '2':
        can_ship1_chase = ship_1.velocity > ship_2.velocity
        if can_ship1_chase:
            while ship_1.pos < ship_2.pos or ship_1.pos - ship_2.pos <= max_distance_between_ships:
                print("=" * 30)
                ship_1.change_pos()
                ship_2.change_pos()
                print(
                    f'{ship_1.name} pos: {ship_1.pos} | {ship_2.name} pos: {ship_2.pos}')
                print("-" * 30)
                print(f'current distance: {ship_2.pos - ship_1.pos: .2f}')
    case '3':
        can_ship2_chase = ship_2.velocity > ship_1.velocity
        if can_ship2_chase:
            while ship_2.pos > ship_1.pos or abs(ship_2.pos - ship_1.pos) <= max_distance_between_ships:
                print("=" * 30)
                ship_1.change_pos(-1)
                ship_2.change_pos(-1)
                print(
                    f'{ship_1.name} pos: {ship_1.pos} | {ship_2.name} pos: {ship_2.pos}')
                print("-" * 30)
                print(f'current distance: {ship_2.pos - ship_1.pos: .2f}')