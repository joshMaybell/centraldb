"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from urllib3 import HTTPResponse

logger: Incomplete

class InfluxDBError(Exception):
    response: Incomplete
    message: Incomplete
    retry_after: Incomplete
    def __init__(
        self, response: HTTPResponse | None = ..., message: str | None = ...
    ) -> None: ...
