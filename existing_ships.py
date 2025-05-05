from ship import Ship
from game_errors import ShipNameNotFound

def get_ship_by_name(ship_name):
    """
    Функция рассчитана на то, что классов кораблей, наций и их особенностей в будущем может стать больше.
    Их можно описать под значение case "New ship name".

    Параметры:
        ship_name (str): имя, для получения готового и существуюего корабля 

    Возвращает экземпляр класса Ship с заготовленными характеристиками корабля
    """

    match ship_name:
        case "Belfast":
            return Ship('Belfast', "Крейсер", "Великобритания", 3000, 14, 30000, 3)
        case "Hood":
            return Ship("Hood", "Линкор", "Великобритания", 6000, 22, 45000, 1.5)
        case "Hipper":
            return Ship("Hipper", "Крейсер", "Германия", 4000, 18, 35000, 2)
        case "Bismarck":
            return Ship("Bismarck", "Линкор", "Германия", 7000, 20, 50000, 1.3)
        case _:
            raise ShipNameNotFound(f'Ship name does not exist: {ship_name}')

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