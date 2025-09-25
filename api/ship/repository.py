from typing import Any

from fastapi import HTTPException, status
import pymongo

from api.db.connection import get_db
from api.db.utils import default_projections
from api.ship.models import ShipInfo


class _ShipsRepository:
  
  def __init__(self):
    self.collaction_name = "ships"
    self.collection = get_db()[self.collaction_name]


  def find_one_by(self, ship_id: str) -> ShipInfo:
    ship_info = self.collection.find_one(ShipInfo.get_battle_ship_by(ship_id), default_projections())
    return ShipInfo.model_validate(ship_info)


  def find_by(self, *ships_id: str) -> list[ShipInfo]:
    return self.find(ShipInfo.get_battle_ships_by(*ships_id))


  def find(self, queries: dict[str, Any] | None=None, **projections: dict[str, Any]) -> list[ShipInfo]:
    ship_infos = self.collection.find(queries, default_projections(**projections))
    return [ShipInfo.model_validate(ship_info) for ship_info in ship_infos]


  def create(self, new_ship: ShipInfo) -> bool:
    try:
      data = new_ship.model_dump(exclude_none=True, exclude_defaults=True)
      print(data)
      action = self.collection.insert_one(data)
      return { "ok": action.acknowledged }
    except pymongo.errors.DuplicateKeyError as e:
      print(e)
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{new_ship.ship_id} is already exists")
    except Exception as e:
      print(e)
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="some error occured")


ShipsRepository = _ShipsRepository()