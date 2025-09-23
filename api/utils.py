from typing import Any

from pydantic import model_validator

from api.ship.models import BattleShipPosition
from engine.ship import Ship

class SetNonesMixin:
    @model_validator(mode='before')
    @classmethod
    def check_card_number_not_present(cls, data: dict[str, Any]) -> Any:
        for field in cls.model_fields.keys():
            if field not in data:
                data.update({field: None})
        return data

def create_ship(info: dict[str, Any], pos: BattleShipPosition) -> Ship:
    battle_ship = Ship(**info)
    battle_ship.set_pos(**pos.model_dump())
    return battle_ship
