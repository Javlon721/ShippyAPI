def get_row_format():
    """
    Функция расчитана для построения таблицы для экземпляров класса Ship.

    Функция возвращает кортеж, где:
        Первое значение - строка шаблон для последующего использования в форматировании
        Второе значение - строка отформатированных названий колонок
    """

    cols = {
        "Название": 15,
        "Тип": 12,
        "Нация": 20,
        "Урон": 8,
        "Дистанция атаки(км)": 22,
        "Очки прочности": 18,
        "Скорость (км/ход)": 20
    }
    template = "".join(["{:<" + str(cols[key]) + "}" for key in cols])
    return (template, template.format(*cols.keys()))


class Ship:
    """
    Класс Ship для создания различных кораблей.

    Параметры:
        name (str): название корабля
        ship_type (str): тип корабля
        nation (str): к какой стране относится корабль
        damage (float): урон корабля
        atack_range (float): дистанция атаки корабля
        hp (float): очки прочности корабля
        velocity (float): Скорость (км / ход)
    """

    _format_template, _formated_titles = get_row_format()

    def __init__(self, name, ship_type, nation, damage, atack_range, hp, velocity):
        # * Я предплолагаю, что данные будут поступать правильные, поэтому обошелся без проверки
        self._name = name
        self._ship_type = ship_type
        self._nation = nation
        self._damage = damage
        self._attack_range = atack_range
        self._hp = hp
        self._velocity = velocity
        self._pos = 0

    @property
    def name(self):
        return self._name

    @property
    def pos(self):
        return round(self._pos, 2)

    @property
    def attack_range(self):
        return self._attack_range
    
    @property
    def velocity(self):
        return self._velocity

    def change_pos(self, direction=1):
        self._pos += self._velocity * direction

    def set_pos(self, val=0):
        self._pos = val

    # * Я хотел использовать cache decorator, но потом передумал.
    # * Буду рад если вы дадите на счет этого коментарий, валидно ли его использовать для этой функциональности.
    def __str__(self):
        return Ship._formated_titles + "\n" + self._get_row

    @property
    def _get_row(self):
        """
        Getter для вывода отформатированного корабля.

        Использует поле класса Ship._format_template для форматирования данных корабля.
        """

        return Ship._format_template.format(
            self._name, self._ship_type, self._nation,
            str(self._damage), str(self._attack_range),
            str(self._hp), str(self._velocity)
        )

    @staticmethod
    def print_ships(ships):
        """
        Выводит список кораблей в отформатированном виде.

        Использует поле класса Ship._formated_titles для отображения заголовков
        и getter экземпляра _get_row для получения строк с данными о каждом корабле.

        Параметры:
            ships (list): Список объектов типа Ship.
        """

        print(Ship._formated_titles)
        for ship in ships:
            print(ship._get_row)


# def main():
#     pass


# if __name__ == "main":
#     main()
