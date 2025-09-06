import json

from game_errors import ShipNameNotFound
from ship import Ship, set_ship_position


def get_ship_by_name(ship_name):
    with open('jsons/ships.json', encoding='UTF-8') as file:
        data = json.load(file)
        ship_info = data.get(ship_name)
        if not ship_info:
            raise ShipNameNotFound(ship_name)
        return Ship(**ship_info)


def input_validated_ship(msg):
    while True:
        try:
            ship = get_ship_by_name(input(msg).strip())
            set_ship_position(ship)
            return ship
        except Exception as e:
            print(f'Ship "{e}" has not found!')


if __name__ == "__main__":
    ship_1 = get_ship_by_name('Belf2ast')
    print(ship_1.modifiers)
