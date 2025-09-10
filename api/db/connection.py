from pymongo import MongoClient

from api.config import DB_CONFIG

client = MongoClient(host=DB_CONFIG.uri)
db = client[DB_CONFIG.dbname]
