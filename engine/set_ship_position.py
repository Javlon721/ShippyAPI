from engine.ship import Ship


def input_validated_number(msg: str) -> float:
    """
    Возвращяет отвалидированное число с плаващей запятой (float) из ввода пользователя
    
    Параметры:
        msg (str) - сообщение, которое выводиться в консоли при вводе данных
    """
    while True:
        try:
            return float(input(msg))
        except Exception:
            print(f'Enter valid number')


def set_ship_position(ship: Ship):
    """
    Функция, которая позволяет получить позицию корабля ((x, y), азимут) от пользователя через консоль,
    после чего применяет эти данные для экземпляря класса Ship
    
    Параметры:
        ship (Ship) - экземпляр класса Ship
    """
    x = input_validated_number(f"Enter {ship.name} 'x' coordinate: ")
    y = input_validated_number(f"Enter {ship.name} 'y' coordinate: ")
    azimuth = input_validated_number(f"Enter {ship.name} azimuth: ")
    set_ship_position_by_values(ship, x, y, azimuth)


def set_ship_position_by_values(ship: Ship, x: float, y: float, azimuth: float):
    ship.set_coords(x, y)
    ship.set_azimuth(azimuth)
