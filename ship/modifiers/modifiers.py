import ship.modifiers.by_ship as by_ship
import ship.modifiers.by_ship_nation as by_ship_nation
import ship.modifiers.by_ship_type as by_ship_type
from itertools import chain, product


class Modifiers:

    def __init__(self, modifiers):
        self.attack_modifiers = []
        self.defence_modifiers = []
        self.get_modifiers_from(modifiers)

    def get_modifiers_from(self, input_modifiers):
        raw_modifiers = self.get_raw_modifiers(input_modifiers)
        for el in chain(by_ship.modifier_list, by_ship_nation.modifier_list, by_ship_type.modifier_list):
            if not len(raw_modifiers):
                break
            modifier_type = raw_modifiers.get(el.__name__, '')
            if not modifier_type:
                continue
            self[modifier_type].append(el)

    def get_raw_modifiers(self, input_modifiers):
        return dict(chain.from_iterable(product(values, [key]) for key, values in input_modifiers.items()))

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
