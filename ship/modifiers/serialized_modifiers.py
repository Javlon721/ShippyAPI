from itertools import chain

import ship.modifiers.by_ship as by_ship
import ship.modifiers.by_ship_nation as by_ship_nation
import ship.modifiers.by_ship_type as by_ship_type


class _SerializeModifiers:

    def __init__(self):
        self._all_modifiers = chain(by_ship.modifier_list, by_ship_nation.modifier_list, by_ship_type.modifier_list)
        self.serialized_modifiers = self._get_serialized_fns()

    def _get_serialized_fns(self):
        return {modifier.__name__: modifier for modifier in self._all_modifiers}

    def get(self, key):
        func = self.serialized_modifiers.get(key, None)
        if not func:
            raise ValueError(f'{type(self).__name__}: {key} not found!')
        return func


serialized_modifiers = _SerializeModifiers()
