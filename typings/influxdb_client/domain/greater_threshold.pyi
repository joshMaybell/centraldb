"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.domain.threshold_base import ThresholdBase

class GreaterThreshold(ThresholdBase):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: str = ...,
        value: Incomplete | None = ...,
        level: Incomplete | None = ...,
        all_values: Incomplete | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
