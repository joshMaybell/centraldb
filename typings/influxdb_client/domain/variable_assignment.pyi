"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.domain.statement import Statement

class VariableAssignment(Statement):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: Incomplete | None = ...,
        id: Incomplete | None = ...,
        init: Incomplete | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def init(self): ...
    @init.setter
    def init(self, init) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
