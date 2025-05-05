def input_validated_number(msg):
    """
    Возвращяет отвалидированное число с плаващей запятой (float) из ввода пользователя
    
    Параметры:
        msg (str) - сообщение, которое выводиться в консоли при вводе данных
    """
    while True:
        try:
            x = float(input(msg))
            break
        except Exception:
            print(f'Enter valid number')
    return x


def set_ship_position(ship):
    """
    Функция, которая позволяет получить позицию корабля ((x, y), азимут) от пользователя через консоль,
    после чего применяет эти данные для экземпляря класса Ship
    
    Параметры:
        ship (Ship) - экземпляр класса Ship
    """
    x = input_validated_number(f"Enter {ship.name} 'x' coordinate: ")
    y = input_validated_number(f"Enter {ship.name} 'y' coordinate: ")
    azimuth = input_validated_number(f"Enter {ship.name} azimuth: ")
    ship.set_coords(x, y)
    ship.set_azimuth(azimuth)
