import ship.modifiers.by_ship as by_ship
import ship.modifiers.by_ship_nation as by_ship_nation
import ship.modifiers.by_ship_type as by_ship_type


class _SerializeModifiers:

    def __init__(self):
        self._modifiers = {}

    @property
    def modifiers(self):
        return self._modifiers

    def register_modifiers(self, modifiers):
        for modifier in modifiers['items']:
            self._modifiers[modifier.__name__] = self._serialize_modifier(modifier, modifiers['priority'])

    def get(self, key):
        func = self._modifiers.get(key)
        if not func:
            raise ValueError(f'{type(self).__name__}: {key} not found!')
        return func

    def _serialize_modifier(self, modifier, priority):
        return Modifier(modifier, priority)


class Modifier:
    slots = ['priority', 'modifier', '__repr__']

    def __init__(self, modifier, priority):
        self.modifier = modifier
        self.priority = priority

    def __repr__(self):
        return f'Modifier(modifier={self.modifier.__name__}, priority={self.priority})'


_serialized_modifiers = _SerializeModifiers()
_serialized_modifiers.register_modifiers(by_ship.options)
_serialized_modifiers.register_modifiers(by_ship_type.options)
_serialized_modifiers.register_modifiers(by_ship_nation.options)


def get_modifier_from(a_name):
    return _serialized_modifiers.get(a_name)


if __name__ == '__main__':
    print(_serialized_modifiers.modifiers)
