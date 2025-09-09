import engine.modifiers.by_ship as by_ship
import engine.modifiers.by_ship_nation as by_ship_nation
import engine.modifiers.by_ship_type as by_ship_type
from engine.modifiers.utils import Modifier, ModifiersOption


class _SerializeModifiers:

    def __init__(self):
        self._modifiers: dict[str, Modifier] = {}

    @property
    def modifiers(self) -> dict[str, Modifier]:
        return self._modifiers

    def register_modifiers(self, modifiers: ModifiersOption):
        for modifier in modifiers.items:
            self._modifiers[modifier.__name__] = Modifier(modifier, modifiers.priority)

    def get(self, key: str) -> Modifier:
        func = self._modifiers.get(key)
        if not func:
            raise ValueError(f'{type(self).__name__}: {key} not found!')
        return func


_serialized_modifiers = _SerializeModifiers()
_serialized_modifiers.register_modifiers(by_ship.options)
_serialized_modifiers.register_modifiers(by_ship_type.options)
_serialized_modifiers.register_modifiers(by_ship_nation.options)


def get_modifier_from(a_name: str) -> Modifier:
    return _serialized_modifiers.get(a_name)


if __name__ == '__main__':
    print(_serialized_modifiers.modifiers)
