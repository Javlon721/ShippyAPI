from fastapi import FastAPI

from api.ship.router import ship_router

app = FastAPI()

app.include_router(ship_router)
