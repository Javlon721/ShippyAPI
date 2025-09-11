from typing import Annotated

from fastapi import APIRouter, Depends

from api.db.connection import db, COLLECTION_TYPE, get_collection
from api.db.utils import default_projections
from api.ship.models import ShipInfo

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
