from existing_ships import get_ship_by_name
from ship import Ship
from game_errors import ShipNameNotFound


while True:
    try:
        ship_1 = get_ship_by_name(input("Enter first ship name: "))
        break
    except ShipNameNotFound as e:
        print(e)
while True:
    try:
        ship_2 = get_ship_by_name(input("Enter second ship name: "))
        break
    except ShipNameNotFound as e:
        print(e)
while True:
    distance_between_ships = input("Enter distance between ships (km): ")
    if distance_between_ships.isdigit():
        distance_between_ships = float(distance_between_ships)
        break
    print('Enter valid number')
while True:
    ships_direction = input("Enter ships direction (0, 1, 2 or 3): ")
    match ships_direction:
        case '0' | "1" | "2" | "3":
            break
        case _:
            print('Enter valid number (0, 1, 2 or 3)')
