from typing import Any

from fastapi import FastAPI

from api.db.connection import client

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/db/healthz")
async def test():
    return client.ships.command("ping")


def default_projections(**options: Any) -> dict[str, Any]:
    print(options)

    options.update({"_id": 0})
    return options


@app.get("/ships/{ship_id}")
def get_ships(ship_id: str):
    return client.ships.ships.find_one({"ship_id": ship_id}, default_projections())


@app.get("/ships")
def get_ships():
    return list(client.ships.ships.find({}, default_projections()))
