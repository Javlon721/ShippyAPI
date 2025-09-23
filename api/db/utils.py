from typing import Any


def default_projections(**options: Any) -> dict[str, Any]:
    options.update({"_id": 0})
    return options
