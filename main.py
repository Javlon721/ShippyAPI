from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.ship.router import ship_router
from api.modifier.router import modifier_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ship_router)
app.include_router(modifier_router)
