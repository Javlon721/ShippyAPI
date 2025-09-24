from typing import Annotated
from pydantic import BaseModel, Field

from engine.ship import Ship


type modifiers_type = Annotated[list[str], Field(default_factory=list)]

class ModifiersModel(BaseModel):
    attack_modifiers: modifiers_type
    defence_modifiers: modifiers_type


class ShipInfo(BaseModel):
    ship_id: str
    hp: int
    velocity: float
    attack_range: float
    damage: int
    modifiers: ModifiersModel = Field(default_factory=ModifiersModel)
    name: str | None = None
    nation: str | None = None
    ship_type: str | None = None

    @staticmethod
    def identify_ship_by(ship_id: str):
        return {
            "ship_id": ship_id.lower(),
        }

    @staticmethod
    def get_battle_ships_by(ship1: str, ship2: str):
        return {
            "ship_id": {"$in": [ship1.lower(), ship2.lower()]}
        }

    @staticmethod
    def get_battle_ship_by(ship_id: str):
        return ShipInfo.identify_ship_by(ship_id)


class BattleShipPosition(BaseModel):
    x: float = 0.0
    y: float = 0.0
    azimuth: float = 0.0


class BattleShip(BaseModel):
    ship_id: str
    coords: BattleShipPosition

    def same_as(self, other: "BattleShip"):
        return self.ship_id == other.ship_id


def create_game_ship(info: ShipInfo, pos: BattleShipPosition) -> Ship:
    battle_ship = Ship(**info.model_dump(exclude_none=True, exclude=["ship_id"]))
    battle_ship.set_pos(**pos.model_dump())
    return battle_ship