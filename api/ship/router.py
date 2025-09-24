import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse


from api.db.connection import db
from api.ship.models import ShipInfo, BattleShip, create_game_ship
from api.ship.repository import ShipsRepository
from engine.main import EOF, start_battle


ship_router = APIRouter(prefix="/ship", tags=["ship"])


@ship_router.get("/db/healthz")
async def test():
    return db.command("ping")


@ship_router.get("/{ship_id}")
def get_ships(ship_id: str) -> ShipInfo:
    return ShipsRepository.find_one_by(ship_id)


@ship_router.get("/", response_model=list[ShipInfo])
def get_ships():
    return ShipsRepository.find()


async def consumer(queue: asyncio.Queue[str]):
    while True:
        msg = await queue.get() 
        if msg == EOF:
            break
        yield msg


@ship_router.post("/battle")
async def get_battle_results(ship1: BattleShip, ship2: BattleShip):
    printer = asyncio.Queue()

    if ship1.same_as(ship2):
        ship = ShipsRepository.find_one_by(ship1.ship_id)
        data = [ship, ship.model_copy(deep=True)]
    else:
        data = ShipsRepository.find_by(ship1.ship_id, ship2.ship_id)

    battle_ship1 = create_game_ship(data[0], ship1.coords)
    battle_ship2 = create_game_ship(data[1], ship2.coords)

    asyncio.create_task(start_battle(battle_ship1, battle_ship2, printer))

    return StreamingResponse(consumer(printer), media_type="text/plain")