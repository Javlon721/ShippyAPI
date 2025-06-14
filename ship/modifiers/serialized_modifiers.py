import ship.modifiers.by_ship as by_ship
import ship.modifiers.by_ship_nation as by_ship_nation
import ship.modifiers.by_ship_type as by_ship_type
from itertools import chain

class _SerializeModifiers:

    def __init__(self):
        self._all_modifiers = chain(by_ship.modifier_list, by_ship_nation.modifier_list, by_ship_type.modifier_list)
        self.serialized_modifiers = self._get_serialized_fns()
    
    def _get_serialized_fns(self):
        return {modifier.__name__: modifier for modifier in self._all_modifiers}
    
    def get(self, key):
        res = self.serialized_modifiers.get(key, None)
        if not res:
            print(f'_SerializeModifiers: {key} not found!')
            return
        return res

serialized_modifiers = _SerializeModifiers()