import asyncio
import functools
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse


from api.db.connection import db, COLLECTION_TYPE, get_collection
from api.db.utils import default_projections
from api.ship.models import ShipInfo, BattleShip
from api.utils import create_ship
from engine.main import EOF, start_battle


ship_router = APIRouter(prefix="/ship", tags=["ship"])
SHIPS_COLLECTION_DEPENDS = Annotated[COLLECTION_TYPE, Depends(get_collection("ships"))]


@ship_router.get("/db/healthz")
async def test():
    return db.command("ping")


@ship_router.get("/{ship_id}")
def get_ships(ship_id: str, collection: SHIPS_COLLECTION_DEPENDS) -> ShipInfo:
    return collection.find_one(ShipInfo.identify_ship_by(ship_id), default_projections())


@ship_router.get("/", response_model=list[ShipInfo])
def get_ships(collection: SHIPS_COLLECTION_DEPENDS):
    return list(collection.find({}, default_projections()))


async def consumer(queue: asyncio.Queue[str]):
    while True:
        msg = await queue.get() 
        if msg == EOF:
            break
        yield msg


@ship_router.post("/battle")
async def get_battle_results(ship1: BattleShip, ship2: BattleShip, collection: SHIPS_COLLECTION_DEPENDS):
    exclude_from_db = default_projections(ship_id=0)
    printer = asyncio.Queue()

    if ship1.same_as(ship2):
        fetched_data = collection.find_one(ShipInfo.get_battle_ship_by(ship1.ship_id), exclude_from_db)
        data = [fetched_data, fetched_data]
    else:
        fetched_data = collection.find(ShipInfo.get_battle_ships_by(ship1.ship_id, ship2.ship_id), exclude_from_db)
        data = list(fetched_data)

    battle_ship1 = create_ship(data[0], ship1.coords)
    battle_ship2 = create_ship(data[1], ship2.coords)

    asyncio.create_task(start_battle(battle_ship1, battle_ship2, printer))

    return StreamingResponse(consumer(printer), media_type="text/plain")
