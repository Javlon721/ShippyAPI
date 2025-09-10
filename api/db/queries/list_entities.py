from collections.abc import Callable
from typing import Mapping, Any, Iterator, Type, TypeVar

T = TypeVar('T')


def serialize_entity(data: Mapping[str, Any], entity_type: Type[T] | Callable[..., T]) -> T:
    return entity_type(**data)


def serialize_entities(ships: Iterator[Mapping[str, Any]], entity_type: Type[T] | Callable[..., T]) -> list[T]:
    return [serialize_entity(ship, entity_type) for ship in ships]
