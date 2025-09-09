import fastapi

from engine.existing_ships import get_ship_by_name_api

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ships/{name}")
async def read_item(name: str):
    return await get_ship_by_name_api(name)
