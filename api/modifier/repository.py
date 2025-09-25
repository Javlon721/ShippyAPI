
from typing import Any

from fastapi import HTTPException, status
from api.db.connection import get_db
from api.db.utils import default_projections
from api.modifier.models import Modifier, ModifiersType


class _ModifiersRepository:
  
  def __init__(self):
    self.collaction_name = "modifiers"
    self.collection = get_db()[self.collaction_name]


  def find_one(self, name: str | None=None, type: ModifiersType | None=None, **projections: dict[str, Any]) -> Modifier:
    info = self.collection.find_one(Modifier.identyfy_by(name=name, type=type), default_projections(**projections))

    if not info:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Modifier.model_validate(info)


  def find(self,  name: str | None=None, type: ModifiersType | None=None, **projections: dict[str, Any]) -> list[Modifier]:
    infos = self.collection.find(Modifier.identyfy_by(name=name, type=type), default_projections(**projections))

    result = [Modifier.model_validate(info) for info in infos]
    if not result:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result




ModifiersRepository = _ModifiersRepository()