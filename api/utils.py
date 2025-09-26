import asyncio
from typing import Any

from pydantic import BaseModel, model_validator


class SetNonesMixin:
    @model_validator(mode='before')
    @classmethod
    def check_card_number_not_present(cls, data: dict[str, Any]) -> Any:
        for field in cls.model_fields.keys():
            if field not in data:
                data.update({field: None})
        return data

class OKResponce(BaseModel):
    ok: bool


async def message_receiver(queue: asyncio.Queue[str], end_flag: str):
    while True:
        msg = await queue.get() 
        if msg == end_flag:
            break
        yield msg