from itertools import chain, product

from ship.modifiers.serialized_modifiers import get_modifier_from_name


class Modifiers:
    # todo add add and remove handlers
    # todo to reuse get_modifier_from_name more natural need get method for this
    def __init__(self, modifiers):
        self.attack_modifiers = []
        self.defence_modifiers = []
        self._set_modifiers_from(modifiers)

    def get_modifier_fn(self, fn_name):
        return get_modifier_from_name(fn_name)

    def _set_modifiers_from(self, input_modifiers):
        raw_modifiers = self._get_raw_modifiers(input_modifiers)

        for fn_name, fn_category in raw_modifiers:
            try:
                self[fn_category].append(self.get_modifier_fn(fn_name))
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
        "attack_modifiesrs": ["bismark_hood", "battleships"],
        "defence_modifiers": ["german_ships"]
    }
    modifiers = Modifiers(example)
    print(modifiers)
