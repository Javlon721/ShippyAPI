from typing import Any


def default_projections(**options: Any) -> dict[str, Any]:
    print(options)

    options.update({"_id": 0})
    return options
