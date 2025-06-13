from math import floor


def cruiser(distance, damage,  attacker, attacked):
    """
    Вычисляет увеличение урона всех крейсеров на amplify (default=4) раз
    Крейсеры наносят в 4 раза больше урона с расстояния в 5 км и ниже (считаем, что у них есть торпеды)

    Параметры:
        damage (float): урон наносимый кораблем
        distance (float): расстояние между кораблями
        attacker (Ship) - экземпляр класса Ship, тот кто атакует
        attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
    """
    amplify_by = 4
    damage_aplify_distance = 5
    if distance <= damage_aplify_distance:
        return damage * amplify_by
    return damage


def battleships(distance, damage,  attacker, attacked):
    """
    Вычисляет уменьшение урона по атакуемым на decrease (default=4)
    Линкоры наносят на 100 урона меньше за каждый километр расстояния, 
    превышающего 10 км (-100 на 11 км, -200 на 12 км и так далее) - считаем, что их бронепробитие падает.

    Параметры:
        damage (float): урон наносимый кораблем
        distance (float): расстояние между кораблями
        attacker (Ship) - экземпляр класса Ship, тот кто атакует
        attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
    """
    decrease = 100
    damage_reduction_distance = 10
    if distance > damage_reduction_distance:
        return damage - (floor(distance) - damage_reduction_distance) * decrease
    return damage


modifier_list = [cruiser, battleships]
