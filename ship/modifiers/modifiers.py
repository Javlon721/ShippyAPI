from enum import Enum
from itertools import chain, product

from ship.modifiers.serialized_modifiers import get_modifier_from


class ModifierType(Enum):
    ATTACK_MODIFIERS = '_attack_modifiers'
    DEFENCE_MODIFIERS = '_defence_modifiers'


class Modifiers:
    def __init__(self, modifiers):
        self._attack_modifiers = []
        self._defence_modifiers = []
        self._set_modifiers_from(modifiers)

    def add_modifier(self, fn_name, modifier_type=ModifierType.ATTACK_MODIFIERS):
        """
            Мылсли:

                можно было сделать сортировку только когда мы получаем значение модификаторов
                сохраняя при этом в кэш, чтоьы при повторном обращении не высчитывать.
                Только при изменении количества модификаторов перемчитывать последовательность

        """
        try:
            target = self._get_modifier_from_db(fn_name)
            index = self._find_proper_index(self[modifier_type.value], target)
            self[modifier_type.value].insert(index, target)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def remove_modifier(self, fn_name, modifier_type=ModifierType.ATTACK_MODIFIERS):
        for index, fn in enumerate(self[modifier_type.value]):
            if fn_name == fn.modifier.__name__:
                self[modifier_type.value].pop(index)
                return index
        raise ValueError(f'{type(self).__name__}: Modifier {fn_name} in {modifier_type.value} not found')

    @property
    def attack_modifiers(self):
        return self._get_modifiers_by(ModifierType.ATTACK_MODIFIERS)

    @property
    def defence_modifiers(self):
        return self._get_modifiers_by(ModifierType.DEFENCE_MODIFIERS)

    def _get_modifiers_by(self, modifier_type):
        return [modifier.modifier for modifier in self[modifier_type.value]]

    def _get_modifier_from_db(self, fn_name):
        return get_modifier_from(fn_name)

    def _set_modifiers_from(self, input_modifiers):
        for fn_name, fn_category in self._get_raw_modifiers(input_modifiers):
            self.add_modifier(fn_name, ModifierType(f'_{fn_category}'))

    def _get_raw_modifiers(self, input_modifiers):
        return chain.from_iterable(product(values, [key]) for key, values in input_modifiers.items())

    def _find_proper_index(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            m = (left + right) // 2
            if arr[m].priority > target.priority:
                right = m
            else:
                left = m + 1
        return left

    def __getitem__(self, value):
        return getattr(self, value)

    def __repr__(self):
        return f'Modifiers: \n attack_modifiers: {self._attack_modifiers} \n defence_modifiers: {self._defence_modifiers}'


if __name__ == "__main__":
    example = {
        "attack_modifiers": ["battleships", "bismark_hood", 'british_ships', 'cruiser', "bismark_hood"],
        "defence_modifiers": ["german_ships", 'cruiser', "bismark_hood"]
    }
    modifiers = Modifiers(example)
    modifiers.remove_modifier('bismark_hood')
    print(modifiers)
    # modifiers.add_modifier('british_ships')
    # modifiers.add_modifier('cruiser')
    # modifiers.remove_modifier('battleships', ModifierType.DEFENCE_MODIFIERS)
    # print('defence', modifiers.defence_modifiers)
