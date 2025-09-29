import pathlib
from dataclasses import dataclass

from pydantic_settings import BaseSettings

env_file = pathlib.Path(__file__).parent.parent / '.env'


@dataclass
class DBConfig:
    dbname: str
    user: str
    password: str
    host: str
    port: int

    @property
    def uri(self) -> str:
        return f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}?authSource=admin"


class _Settings(BaseSettings):
    # Mongodb
    MONGODB_USER: str
    MONGODB_PASS: str
    MONGODB_DBNAME: str
    MONGODB_HOST: str
    MONGODB_PORT: int

    def db_config(self) -> DBConfig:
        return DBConfig(
            dbname=self.MONGODB_DBNAME,
            user=self.MONGODB_USER,
            password=self.MONGODB_PASS,
            host=self.MONGODB_HOST,
            port=self.MONGODB_PORT,
        )


SETTINGS = _Settings(_env_file=env_file)
DB_CONFIG = SETTINGS.db_config()
