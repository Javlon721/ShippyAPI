from ship import Ship


def get_ship_by_name(ship_name):
    """
    Функция расчитана для построения таблицы для экземпляров класса Ship.
    
    Функция возвращает кортеж, где:
        Первое значение - строка шаблон для последующего использования в форматировании
        Второе значение - строка отформатированных названий колонок
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


ship_1 = get_ship_by_name("Belfast")
ship_2 = get_ship_by_name("Hood")

# print(ship_1 )
Ship.print_ships([ship_1, ship_2])