from pydantic import BaseModel


class ModifiersModel(BaseModel):
    attack_modifiers: list[str] | None = None
    defence_modifiers: list[str] | None = None


class ShipCreateInfo(BaseModel):
    ship_id: str
    hp: int
    velocity: float
    attack_range: float
    damage: int
    modifiers: ModifiersModel | None = None
    name: str | None = None
    nation: str | None = None
    ship_type: str | None = None
