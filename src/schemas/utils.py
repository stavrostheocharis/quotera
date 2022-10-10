from pydantic import BaseModel
from enum import Enum


class Redirection(BaseModel):
    """Codes 300 and above are for "Redirection."""

    pass


class ClientError(BaseModel):
    """Codes 400 and above are for "Client error" responses."""

    detail: str


class ServerError(BaseModel):
    """500 and above are for server errors."""

    detail: str


class HealthCheck(BaseModel):
    status: str
