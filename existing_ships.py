from ship import Ship
from game_errors import ShipNameNotFound
import json


def get_ship_by_name(ship_name):
    """
    Функция рассчитана на то, что классов кораблей, наций и их особенностей в будущем может стать больше.
    Их можно описать под значение case "New ship name".

    Параметры:
        ship_name (str): имя, для получения готового и существуюего корабля 

    Возвращает экземпляр класса Ship с заготовленными характеристиками корабля
    """

    with open('jsons/ships.json', encoding='UTF-8') as file:
        data = json.load(file)
        for item in data:
            if item['name'] == ship_name:
                return Ship(**item)

        raise ShipNameNotFound(f'Ship "{ship_name}" has not found!')


def input_validated_ship(msg):
    """
    Возвращяет отвалидированный экземпляр класса Ship из ввода пользователя

    Параметры:
        msg (str) - сообщение, которое выводиться в консоли при вводе данных
    """
    while True:
        try:
            ship = get_ship_by_name(input(msg).strip())
            break
        except ShipNameNotFound as e:
            print(e)
    return ship


if __name__ == "__main__":
    ship_1 = get_ship_by_name('Belfast')
    print(ship_1.modifiers)
