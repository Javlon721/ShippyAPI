def bismark_hood(distance, damage,  attacker, attacked):
    """
    Bismarck наносит двойной урон по Hood с расстояния от 15 до 18 км

    Параметры:
        damage (float): урон наносимый кораблем
        distance (float): расстояние между кораблями
        attacker (Ship) - экземпляр класса Ship, тот кто атакует
        attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
    """

    if attacked.name == "Hood" and 15 <= distance <= 18:
        return damage * 2
    return damage


modifier_list = [bismark_hood]
