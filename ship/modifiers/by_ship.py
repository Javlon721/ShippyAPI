from ship.modifiers.utils import ModifiersPriority, ModifiersOption, register_modifier

options = ModifiersOption(priority=ModifiersPriority.BY_SHIP)

register = register_modifier(options)


@register
def bismark_hood(distance, damage, attacker, attacked):
    """
    Bismarck наносит двойной урон по Hood с расстояния от 15 до 18 км

    Параметры:
        damage (float): урон наносимый кораблем
        distance (float): расстояние между кораблями
        attacker (Ship) - экземпляр класса Ship, тот кто атакует
        attacked (Ship) - экземпляр класса Ship, тот корорый получает урон
    """
    bismark_amplify_targets = ['Hood']
    max_amplify_distance = 18
    min_amplify_distance = 15
    amplify_by = 2
    if (attacked.name in bismark_amplify_targets) and (min_amplify_distance <= distance <= max_amplify_distance):
        return damage * amplify_by
    return damage


if __name__ == '__main__':
    print(options)
