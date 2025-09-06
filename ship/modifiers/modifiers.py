from enum import Enum
from itertools import chain, product
from typing import Iterable, Any

from ship.modifiers.serialized_modifiers import get_modifier_from
from ship.modifiers.utils import Modifier, bin_search, ModifierFn


class ModifierType(Enum):
    attack = 'attack_modifiers'
    defence = 'defence_modifiers'


type RawModifiers = dict[str, list[str]]
type SerializedModifiers = list[Modifier]


class Modifiers:
    def __init__(self, modifiers: RawModifiers):
        self.attack_modifiers: SerializedModifiers = []
        self.defence_modifiers: SerializedModifiers = []
        self._set_modifiers_from(modifiers)

    def add_modifier(self, fn_name: str, modifier_type: ModifierType):
        """
            Мылсли:

                можно было сделать сортировку только когда мы получаем значение модификаторов
                сохраняя при этом в кэш, чтоьы при повторном обращении не высчитывать.
                Только при изменении количества модификаторов перемчитывать последовательность

        """

        try:
            target = self._get_modifier_from_db(fn_name)
            modifiers = self[modifier_type.value]
            index = bin_search(0, len(modifiers), modifiers, target, Modifiers.compare_priority)
            modifiers.insert(index, target)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def remove_modifier(self, fn_name: str, modifier_type: ModifierType) -> int | None:
        for index, fn in enumerate(self[modifier_type.value]):
            if fn_name == fn.modifier.__name__:
                self[modifier_type.value].pop(index)
                return index
        raise ValueError(f'{type(self).__name__}: Modifier {fn_name} in {modifier_type.value} not found')

    @property
    def attack_fns(self) -> list[ModifierFn]:
        return self._get_modifiers_by(ModifierType.attack)

    @property
    def defence_fns(self) -> list[ModifierFn]:
        return self._get_modifiers_by(ModifierType.defence)

    @classmethod
    def compare_priority(cls, m1: Modifier, m2: Modifier) -> bool:
        return m1.priority > m2.priority

    def _get_modifiers_by(self, modifier_type: ModifierType) -> list[ModifierFn]:
        return [modifier.modifier for modifier in self[modifier_type.value]]

    def _get_modifier_from_db(self, fn_name: str) -> Modifier:
        return get_modifier_from(fn_name)

    def _set_modifiers_from(self, input_modifiers: RawModifiers):
        for fn_name, fn_category in self._get_raw_modifiers(input_modifiers):
            self.add_modifier(fn_name, ModifierType(fn_category))

    def _get_raw_modifiers(self, input_modifiers: RawModifiers) -> Iterable[tuple[str, str]]:
        return chain.from_iterable(product(values, [key]) for key, values in input_modifiers.items())

    def __getitem__(self, value: str) -> Any:
        return getattr(self, value)

    def __repr__(self) -> str:
        return f'Modifiers: \n attack_modifiers: {self.attack_modifiers} \n defence_modifiers: {self.defence_modifiers}'


if __name__ == "__main__":
    example = {
        "attack_modifiers": ["battleships", "bismark_hood", 'british_ships', 'cruiser', "bismark_hood"],
        "defence_modifiers": ["german_ships", 'cruiser', "bismark_hood"]
    }
    modifiers = Modifiers(example)
    modifiers.remove_modifier('bismark_hood', ModifierType.attack)
    print(modifiers)
    # modifiers.add_modifier('british_ships')
    # modifiers.add_modifier('cruiser')
    # modifiers.remove_modifier('battleships', ModifierType.defence)
    # print('defence', modifiers.defence_modifiers)
