from enum import Enum
from itertools import chain, product

from ship.modifiers.serialized_modifiers import get_modifier_from_name
from ship.utils import bin_search


class ModifierType(Enum):
    ATTACK_MODIFIERS = '_attack_modifiers'
    DEFENCE_MODIFIERS = '_defence_modifiers'


class Modifiers:
    # todo упростить это "явление" кода
    def __init__(self, modifiers):
        self._attack_modifiers = []
        self._defence_modifiers = []
        self._set_modifiers_from(modifiers)

    def add_modifier(self, fn_name, modifier_type=ModifierType.ATTACK_MODIFIERS):
        try:
            target = self._get_modifier_fn(fn_name)
            index = bin_search(self[modifier_type.value], target,
                               lambda m, arr, target: arr[m].priority > target.priority)
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
        return self._get_modifiers_fn(ModifierType.ATTACK_MODIFIERS)

    @property
    def defence_modifiers(self):
        return self._get_modifiers_fn(ModifierType.DEFENCE_MODIFIERS)

    def _get_modifiers_fn(self, modifier_type):
        return [modifier.modifier for modifier in self[modifier_type.value]]

    def _get_modifier_fn(self, fn_name):
        return get_modifier_from_name(fn_name)

    def _set_modifiers_from(self, input_modifiers):
        raw_modifiers = self._get_raw_modifiers(input_modifiers)

        for fn_name, fn_category in raw_modifiers:
            try:
                self.add_modifier(fn_name, ModifierType(f'_{fn_category}'))
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)

    def _get_raw_modifiers(self, input_modifiers):
        return chain.from_iterable(product(values, [key]) for key, values in input_modifiers.items())

    def __getitem__(self, value):
        return getattr(self, value)

    def __repr__(self):
        return f'Modifiers: \n attack_modifiers: {self._attack_modifiers} \n defence_modifiers: {self._defence_modifiers}'


if __name__ == "__main__":
    example = {
        "attack_modifiers": ["battleships", "bismark_hood", 'british_ships', 'cruiser', "bismark_hood"],
        "defence_modifiers": ["german_ships"]
    }
    modifiers = Modifiers(example)
    modifiers.remove_modifier('bismark_hood')
    print(modifiers)
    # modifiers.add_modifier('british_ships')
    # modifiers.add_modifier('cruiser')
    # modifiers.remove_modifier('battleships', ModifierType.DEFENCE_MODIFIERS)
    # print('defence', modifiers.defence_modifiers)
