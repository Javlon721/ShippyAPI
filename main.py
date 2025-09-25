from fastapi import FastAPI

from api.ship.router import ship_router
from api.modifier.router import modifier_router

app = FastAPI()

app.include_router(ship_router)
app.include_router(modifier_router)
