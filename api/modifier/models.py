from typing import Literal

from pydantic import BaseModel, Field


type ModifiersType = Literal["attack", "defence"]


class Modifier(BaseModel):

  name: str = Field(min_length=5)
  desc: str = ""
  type: ModifiersType


  @staticmethod
  def identyfy_by(name: str | None=None, type: ModifiersType | None=None) -> dict[str, str]:
    result = {}

    if name:
      result["name"] =  name.lower().strip()

    if type:
      result["type"] =  type

    return result

