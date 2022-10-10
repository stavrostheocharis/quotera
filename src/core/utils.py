import json
from typing import Any, Dict
from pydantic.json import pydantic_encoder


def pydantic_json_serializer(body: Dict[str, Any]) -> str:
    """
    Use it with aiohttp client for dictionaries tha include or are themselves a pydantic object.
    """
    return json.dumps(body, default=pydantic_encoder)
