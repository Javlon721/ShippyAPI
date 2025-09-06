from ship.modifiers.modifiers import Modifiers
from ship.util_classes import Coords, Azimuth
from itertools import chain


def get_row_format():
    """
    Функция расчитана для построения таблицы вывода информации для экземпляров класса Ship.

    Функция возвращает кортеж, где:
        Первое значение - строка шаблон для последующего использования в форматировании
        Второе значение - строка отформатированных названий колонок

    Для использования метода template.format используйте последовательность ключей словаря
    cols - ("Название", "Тип", "Нация", "Урон", "Дистанция атаки(км)", "Очки прочности", "Скорость (км/ход)", "Координаты",
    "Азимут")
    """

    cols = {
        "Название": 15,
        "Тип": 12,
        "Нация": 20,
        "Урон": 8,
        "Дистанция атаки(км)": 22,
        "Очки прочности": 18,
        "Скорость (км/ход)": 20,
        "Координаты": 15,
        "Азимут": 6,
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
        attack_range (float): дистанция атаки корабля
        hp (float): очки прочности корабля
        velocity (float): Скорость (км / ход)
    """

    _format_template, _formated_titles = get_row_format()

    def __init__(self, name, ship_type, nation, damage, attack_range, hp, velocity, modifiers):
        self.name = name
        self.ship_type = ship_type
        self.nation = nation
        self.damage = damage
        self.attack_range = attack_range
        self.hp = hp
        self.velocity = velocity
        self.coords = Coords(0, 0)
        self.azimuth = Azimuth(0)
        self.modifiers = Modifiers(modifiers)

    @staticmethod
    def apply_modifiers(attacker, attacked):
        """
        Применяет модификаторы атакующего (attacker), а после модификаторы атакуемого (attacked) 
        к рассчету урона атакующего

        Параметры:
            attacker (Ship) - экземпляр класса Ship, тот кто атакует
            attacked (Ship) - экземпляр класса Ship, тот который получает урон
        """
        distance = attacker.get_distance_between(attacked)
        damage = attacker.damage
        for fn in chain(attacker.modifiers.attack_modifiers, attacked.modifiers.defence_modifiers):
            damage = fn(distance, damage, attacker, attacked)
        return damage

    def change_coords(self):
        self.coords.change_coords(self.velocity, self.azimuth.azimuth_in_rad)

    def set_coords(self, x, y):
        self.coords.x = x
        self.coords.y = y

    def set_azimuth(self, azimuth):
        self.azimuth.set_azimuth(azimuth)

    def get_distance_between(self, ship):
        """
        Функция нахождения расстояние между двумя точками по их координатам, если заданы две точки:
            A с координатами (x1, y1)
            B с координатами (x2, y2)
        то расстояние между ними вычисляется по формуле:
        distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        """
        distance = ((self.coords.x - ship.coords.x)
                    ** 2 + (self.coords.y - ship.coords.y) ** 2) ** 0.5
        return round(distance, 2)

    def can_attack(self, ship):
        return self.get_distance_between(ship) <= self.attack_range

    def attack(self, ship):
        if not self.can_attack(ship):
            # print(f'{ship.name} is too far (distance is {self.get_distance_between(ship): .02f} when expecting {self.attack_range}) or {self.name} was destroyed ({self.name} healthpoint is {self.hp})')
            pass
        else:
            total_damage = Ship.apply_modifiers(attacker=self, attacked=ship)
            print(
                f'{self.name} hit {ship.name} with {total_damage} damage.')
            ship.receive_damage(total_damage)

    def is_alive(self):
        return self.hp > 0

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if not self.is_alive():
            print(f'{self.name} has been destroyed!')

    def __str__(self):
        return Ship._formated_titles + "\n" + self._get_row

    @property
    def _get_row(self):
        return Ship._format_template.format(
            self.name, self.ship_type, self.nation,
            str(self.damage), str(self.attack_range),
            str(self.hp), str(self.velocity), str(
                (self.coords.x, self.coords.y)), str(self.azimuth.azimuth)
        )

    @staticmethod
    def print_ships(*ships):
        """
        Выводит список кораблей в отформатированном виде.

        Использует поле класса Ship._formated_titles для отображения заголовков
        и getter экземпляра _get_row для получения строк с данными о каждом корабле.

        Параметры:
            ships (*ships): Неограниченное количество объектов Ship, переданных как аргументы
        """

        print(Ship._formated_titles)
        for ship in ships:
            print(ship._get_row)
