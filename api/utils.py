from typing import Any

from pydantic import model_validator


class SetNonesMixin:
    @model_validator(mode='before')
    @classmethod
    def check_card_number_not_present(cls, data: dict[str, Any]) -> Any:
        for field in cls.model_fields.keys():
            if field not in data:
                data.update({field: None})
        return data
