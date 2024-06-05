"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class ShardGroupManifest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        start_time: Incomplete | None = ...,
        end_time: Incomplete | None = ...,
        deleted_at: Incomplete | None = ...,
        truncated_at: Incomplete | None = ...,
        shards: Incomplete | None = ...,
    ) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def start_time(self): ...
    @start_time.setter
    def start_time(self, start_time) -> None: ...
    @property
    def end_time(self): ...
    @end_time.setter
    def end_time(self, end_time) -> None: ...
    @property
    def deleted_at(self): ...
    @deleted_at.setter
    def deleted_at(self, deleted_at) -> None: ...
    @property
    def truncated_at(self): ...
    @truncated_at.setter
    def truncated_at(self, truncated_at) -> None: ...
    @property
    def shards(self): ...
    @shards.setter
    def shards(self, shards) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
