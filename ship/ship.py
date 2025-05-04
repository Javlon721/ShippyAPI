from ship.modifiers import by_ship_type, by_ship_nation, by_ship
from itertools import chain


def get_row_format():
    """
    Функция расчитана для построения таблицы для экземпляров класса Ship.

    Функция возвращает кортеж, где:
        Первое значение - строка шаблон для последующего использования в форматировании
        Второе значение - строка отформатированных названий колонок

    Для использования метода template.format используйте последовательность ключей словаря
    cols - ("Название", "Тип", "Нация", "Урон", "Дистанция атаки(км)", "Очки прочности", "Скорость (км/ход)", "Местонахождение (по координате х)")
    """

    cols = {
        "Название": 15,
        "Тип": 12,
        "Нация": 20,
        "Урон": 8,
        "Дистанция атаки(км)": 22,
        "Очки прочности": 18,
        "Скорость (км/ход)": 20,
        "Местонахождение (по координате х)": 35,
    }
    template = "".join(["{:<" + str(cols[key]) + "}" for key in cols])
    return (template, template.format(*cols.keys()))


modifiers = {
    "by_ship_type": {
        'Крейсер': [by_ship_type.cruiser],
        'Линкор': [by_ship_type.battleships],
    },
    "by_ship_nation": {
        "Великобритания": [by_ship_nation.british_ships],
        "Германия": [by_ship_nation.german_ships],
    },
    "by_ship": {
        "Bismarck": [by_ship.bismark_hood],
    },
}


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
        self.name = name
        self.ship_type = ship_type
        self.nation = nation
        self.damage = damage
        self.attack_range = atack_range
        self.hp = hp
        self.velocity = velocity
        self.pos = 0
        self.attack_modifiers = modifiers["by_ship"].get(self.name, []) \
            + modifiers["by_ship_type"].get(self.ship_type, [])
        self.defence_modifiers = modifiers["by_ship_nation"].get(
            self.nation, [])

    @staticmethod
    def apply_modifiers(attacker, attacked):
        """
        Применяет модификаторы атакующего (attacker), а после модификаторы атакуемого (attacked) 
        к рассчету урона (damage)

        Параметры:
            attacker (Ship) - экземпляр класса Ship, тот кто атакует
            attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
        """
        distance = attacker.get_distance_between(attacked)
        damage = attacker.damage
        for fn in chain(attacker.attack_modifiers, attacked.defence_modifiers):
            print(f"Before {fn.__name__} modifier damage is {damage}")
            damage = fn(distance, damage, attacker, attacked)
            print(f"After {fn.__name__} modifier damage is {damage}")
        return damage

    def change_pos(self, direction=1):
        self.pos += self.velocity * direction

    def set_pos(self, val=0):
        self.pos = val

    def get_distance_between(self, ship):
        return abs(self.pos - ship.pos)

    def can_attack(self, ship):
        return self.get_distance_between(ship) <= self.attack_range and self.is_alive()

    def attack(self, ship):
        print('-' * 30)
        print(f'{self.name} at {self.pos} while {ship.name} at {ship.pos}. Distence between ships is {self.get_distance_between(ship)}')
        print(
            f'{self.name} is attacking {ship.name}. {ship.name} healthpoint is {ship.hp}')
        if not self.can_attack(ship):
            print(f'{ship.name} is too far (distance is {self.get_distance_between(ship)} when expecting {self.attack_range}) or {self.name} was destroyed (current healthpoint is {self.hp})')
        else:
            total_damage = Ship.apply_modifiers(attacker=self, attacked=ship)
            ship.receive_damage(total_damage)
            print(
                f'{self.name} hit {ship.name} with {total_damage} damage. {ship.name} healthpoint is {ship.hp}')

    def is_alive(self):
        return self.hp > 0

    def receive_damage(self, damage):
        if not self.is_alive():
            print(f'{self.name} has already destroyed!')
        else:
            self.hp = max(0, self.hp - damage)

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
            self.name, self.ship_type, self.nation,
            str(self.damage), str(self.attack_range),
            str(self.hp), str(self.velocity), str(self.pos)
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
