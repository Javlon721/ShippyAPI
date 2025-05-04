def create_attack_checker(ship1, ship2):
    """
    Функция возвращает другую функцию с замкнутыми параметрами
        ship1 (Ship) - экземпляр класса Ship
        ship2 (Ship) - экземпляр класса Ship
    рассчитывает сможет ли хотябы 1 из них атаковать за ход
    """
    # * Я замкнул параметры (ship1, ship2), чтобы в функции calculate_moves
    # * при неоднократном вызове функции can_any_attack не дублировать передачу параметров.
    # * Буду рад если вы дадите коментарий к такому подходу!

    max_attack_distance = max(ship1.attack_range, ship2.attack_range)

    def can_any_attack():
        return ship1.get_distance_between(ship2) <= max_attack_distance
    return can_any_attack


def ships_battle_per_move(ship1, ship2):
    print(
        f'Distence between {ship1.name} and {ship2.name} is {ship1.get_distance_between(ship2): .02f}')
    ship1.attack(ship2)
    ship2.attack(ship1)
    print()


def is_both_alive(ship1, ship2):
    return ship1.is_alive() and ship2.is_alive()


def calculate_moves(ship1, ship2, ships_direction):
    can_any_attack = create_attack_checker(ship1, ship2)
    match ships_direction:
        case '0':
            """
            Пока ship2 приближается к ship1 или один из них или оба могут атаковать (ship_1 -> <- ship_2)
            """
            while ship2.pos > ship1.pos or can_any_attack():
                ships_battle_per_move(ship1, ship2)
                if not is_both_alive(ship1, ship2):
                    break
                ship1.change_pos()
                ship2.change_pos(-1)
        case '1':
            """
            Пока один из них или оба могут атаковать (<- ship_1  ship_2 ->)
            """
            while can_any_attack():
                ships_battle_per_move(ship1, ship2)
                if not is_both_alive(ship1, ship2):
                    break
                ship1.change_pos(-1)
                ship2.change_pos()
        case '2':
            """
            Пока ship1 догоняет ship2 или расстояние между ними такое, что один из них или оба могут атаковать
            (ship_1 -> ship_2 ->)
            """
            while (ship2.pos > ship1.pos and ship1.velocity > ship2.velocity) or can_any_attack():
                ships_battle_per_move(ship1, ship2)
                if not is_both_alive(ship1, ship2):
                    break
                ship1.change_pos()
                ship2.change_pos()
        case '3':
            """
            Пока ship2 догоняет ship1 или расстояние между ними такое, что один из них или оба могут атаковать
            (<- ship_1 <- ship_2 )
            """
            while (ship2.pos > ship1.pos and ship2.velocity > ship1.velocity) or can_any_attack():
                ships_battle_per_move(ship1, ship2)
                if not is_both_alive(ship1, ship2):
                    break
                ship1.change_pos(-1)
                ship2.change_pos(-1)
