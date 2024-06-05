"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class PingService(_BaseService):
    def __init__(self, api_client: Incomplete | None = ...) -> None: ...
    def get_ping(self, **kwargs): ...
    def get_ping_with_http_info(self, **kwargs): ...
    async def get_ping_async(self, **kwargs): ...
    def head_ping(self, **kwargs): ...
    def head_ping_with_http_info(self, **kwargs): ...
    async def head_ping_async(self, **kwargs): ...
