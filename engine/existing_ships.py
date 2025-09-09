import json
import pathlib
from typing import Any

import aiofiles

from engine.game_errors import ShipNameNotFound
from engine.set_ship_position import set_ship_position
from engine.ship import Ship

path_to_ships = pathlib.Path(__file__).parent.parent / 'jsons' / 'ships.json'


def get_ship_by_name(ship_name: str) -> Ship:
    with open(path_to_ships, encoding='UTF-8') as file:
        data = json.load(file)
        ship_name = ship_name.lower()
        ship_info = data.get(ship_name)
        if not ship_info:
            raise ShipNameNotFound(ship_name)
        return Ship(**ship_info)


async def get_ship_by_name_api(ship_name: str) -> dict[str, Any]:
    async with aiofiles.open(path_to_ships, encoding='UTF-8') as file:
        content = await file.read()  # Read file content as string
        data = json.loads(content)  # Parse
        ship_name = ship_name.lower()
        ship_info = data.get(ship_name)
        if not ship_info:
            raise ShipNameNotFound(ship_name)
        return ship_info


def input_validated_ship(msg: str) -> Ship:
    while True:
        try:
            ship = get_ship_by_name(input(msg).strip())
            set_ship_position(ship)
            return ship
        except Exception as e:
            print(f'Ship "{e}" has not found!')


if __name__ == "__main__":
    ship_1 = get_ship_by_name('Belfast')
    print(ship_1.modifiers)
