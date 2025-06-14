from itertools import chain, product
from ship.modifiers.serialized_modifiers import serialized_modifiers

class Modifiers:

    def __init__(self, modifiers):
        self.attack_modifiers = []
        self.defence_modifiers = []
        self._set_modifiers_from(modifiers)

    def _set_modifiers_from(self, input_modifiers):
        raw_modifiers= self._get_raw_modifiers(input_modifiers)

        for fn_name, fn_category in raw_modifiers:
            fn = serialized_modifiers.get(fn_name)
            if not fn:
                print(f'{fn_name} not found!')
                continue
            self[fn_category].append(fn)

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
        "attack_modifiers": ["bismark_hood", "battleships"],
        "defence_modifiers": ["german_ships"]
    }
    modifiers = Modifiers(example)
    print(modifiers)
