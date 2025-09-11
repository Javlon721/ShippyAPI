from typing import Callable

from pymongo import MongoClient
from pymongo.database import Database, Collection

from api.config import DB_CONFIG

client = MongoClient(host=DB_CONFIG.uri)
db = client[DB_CONFIG.dbname]

DB_TYPE = Database
COLLECTION_TYPE = Collection


def get_db() -> DB_TYPE:
    return db


def get_collection(collection_name: str) -> Callable[[], COLLECTION_TYPE]:
    def wrapper() -> COLLECTION_TYPE:
        return db[collection_name]

    return wrapper
