"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.domain.expression import Expression

class DurationLiteral(Expression):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, type: Incomplete | None = ..., values: Incomplete | None = ...
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def values(self): ...
    @values.setter
    def values(self, values) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
