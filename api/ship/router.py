from typing import Any

from fastapi import APIRouter

from api.db.connection import client

ship_router = APIRouter(prefix="/ship", tags=["ship"])


@ship_router.get("/db/healthz")
async def test():
    return client.ships.command("ping")


def default_projections(**options: Any) -> dict[str, Any]:
    print(options)

    options.update({"_id": 0})
    return options


@ship_router.get("/{ship_id}")
def get_ships(ship_id: str):
    return client.ships.ships.find_one({"ship_id": ship_id}, default_projections())


@ship_router.get("/")
def get_ships():
    return list(client.ships.ships.find({}, default_projections()))
