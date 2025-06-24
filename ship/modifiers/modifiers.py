from enum import Enum
from itertools import chain, product

from ship.modifiers.serialized_modifiers import get_modifier_from_name
from ship.utils import bin_search


class ModifierType(Enum):
    ATTACK_MODIFIERS = 'attack_modifiers'
    DEFENCE_MODIFIERS = 'defence_modifiers'


class Modifiers:
    # todo упростить это "явление" кода
    def __init__(self, modifiers):
        self.attack_modifiers = []
        self.defence_modifiers = []
        self._set_modifiers_from(modifiers)

    def get_modifier_fn(self, fn_name):
        return get_modifier_from_name(fn_name)

    def add_modifier(self, fn_name, modifier_type=ModifierType.ATTACK_MODIFIERS):
        try:
            target = self.get_modifier_fn(fn_name)
            index = bin_search(self[modifier_type.value], target,
                               lambda m, arr, target: arr[m]['priority'] > target['priority'])
            self[modifier_type.value].insert(index, target)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def remove_modifier(self, fn_name, modifier_type=ModifierType.ATTACK_MODIFIERS):
        for index, fn in enumerate(self[modifier_type.value]):
            if fn_name == fn.__name__:
                self[modifier_type.value].remove(fn)
                return index
        raise ValueError(f'{type(self).__name__}: Modifier {fn_name} in {modifier_type.value} not found')

    def _set_modifiers_from(self, input_modifiers):
        raw_modifiers = self._get_raw_modifiers(input_modifiers)

        for fn_name, fn_category in raw_modifiers:
            try:
                self.add_modifier(fn_name, ModifierType(fn_category))
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)

    def _get_raw_modifiers(self, input_modifiers):
        return chain.from_iterable(product(values, [key]) for key, values in input_modifiers.items())

    def __getitem__(self, value):
        return getattr(self, value)

    def _extract_fns_name(self, fns, separator=', '):
        return separator.join([fn.__name__ for fn in fns])

    def __repr__(self):
        return f'Modifiers: \n attack_modifiers: {self._extract_fns_name(self.attack_modifiers)} \n defence_modifiers: {self._extract_fns_name(self.defence_modifiers)}'


if __name__ == "__main__":
    example = {
        "attack_modifiers": ["battleships", "bismark_hood", 'british_ships', 'cruiser', "bismark_hood"],
        "defence_modifiers": ["german_ships"]
    }
    modifiers = Modifiers(example)
    # modifiers.add_modifier('british_ships')
    # modifiers.add_modifier('cruiser')
    modifiers.add_modifier('bismark_hood', ModifierType.DEFENCE_MODIFIERS)
    # modifiers.remove_modifier('battleships', ModifierType.DEFENCE_MODIFIERS)
    for el in modifiers.attack_modifiers:
        print(el['priority'])
    # print('defence', modifiers.defence_modifiers)
