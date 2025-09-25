
from fastapi import APIRouter

from api.modifier.models import ModifiersType, Modifier
from api.modifier.repository import ModifiersRepository


modifier_router = APIRouter(prefix="/modifier", tags=['modifier'])


@modifier_router.get("/{modifier_name}")
def get_modifier_by(modifier_name: str):
  return ModifiersRepository.find_one(modifier_name, type=None)


@modifier_router.get("/")
def get_modifiers(name: str | None=None, type: ModifiersType | None=None):
  return ModifiersRepository.find(name, type)