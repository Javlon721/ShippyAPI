from typing import Annotated

from fastapi import APIRouter, Depends

from api.db.connection import db, COLLECTION_TYPE, get_collection
from api.db.utils import default_projections
from api.ship.models import ShipInfo, BattleShip
from engine.main import start_battle
from engine.set_ship_position import set_ship_position_by_values
from engine.ship import Ship

ship_router = APIRouter(prefix="/ship", tags=["ship"])
SHIPS_COLLECTION_DEPENDS = Annotated[COLLECTION_TYPE, Depends(get_collection("ships"))]


@ship_router.get("/db/healthz")
async def test():
    return db.command("ping")


@ship_router.get("/{ship_id}")
def get_ships(ship_id: str, collection: SHIPS_COLLECTION_DEPENDS):
    return collection.find_one(ShipInfo.identify_ship_by(ship_id), default_projections())


@ship_router.get("/")
def get_ships(collection: SHIPS_COLLECTION_DEPENDS):
    return list(collection.find({}, default_projections()))


@ship_router.post("/battle")
def get_ships(ship1: BattleShip, ship2: BattleShip, collection: SHIPS_COLLECTION_DEPENDS):
    exclude_from_db = default_projections(ship_id=0)

    if ship1.same_as(ship2):
        fetched_data = collection.find_one(ShipInfo.get_battle_ship_by(ship1.ship_id), exclude_from_db)
        data = [fetched_data, fetched_data]
    else:
        data = list(
            collection.find(ShipInfo.get_battle_ships_by(ship1.ship_id, ship2.ship_id), exclude_from_db))

    battle_ship1 = Ship(**data[0])
    set_ship_position_by_values(battle_ship1, ship1.coords.x, ship1.coords.y, ship1.coords.azimuth)

    battle_ship2 = Ship(**data[1])
    set_ship_position_by_values(battle_ship2, ship2.coords.x, ship2.coords.y, ship2.coords.azimuth)

    start_battle(battle_ship1, battle_ship2)

    return battle_ship1, battle_ship2
