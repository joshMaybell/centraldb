"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete
import logging

class InfluxLoggingHandler(logging.Handler):
    DEFAULT_LOG_RECORD_KEYS: Incomplete
    bucket: Incomplete
    client: Incomplete
    write_api: Incomplete
    def __init__(
        self,
        *,
        url,
        token,
        org,
        bucket,
        client_args: Incomplete | None = ...,
        write_api_args: Incomplete | None = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def emit(self, record: logging.LogRecord) -> None: ...
