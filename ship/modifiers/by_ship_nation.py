def british_ships(distance, damage, attacker, attacked):
    """
    Все британские корабли игнорируют половину урона (с округлением вниз) 
    если он нанесён с расстояния больше 8 км (считаем, что по ним тяжело попасть с такой дистанции).

    Параметры:
        damage (float): урон наносимый кораблем
        distance (float): расстояние между кораблями
        attacker (Ship) - экземпляр класса Ship, тот кто атакует
        attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
    """
    ignore_distance = 8
    ingnore_damage = 2
    if distance >= ignore_distance:
        return damage // ingnore_damage
    return damage


def german_ships(distance, damage,  attacker, attacked):
    """
    Все немецкие корабли получают на 20% урона меньше.

    Параметры:
        damage (float): урон наносимый кораблем
        distance (float): расстояние между кораблями
        attacker (Ship) - экземпляр класса Ship, тот кто атакует
        attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
    """
    ignore_damage = 0.8
    return damage * ignore_damage


modifier_list = [british_ships, german_ships]
