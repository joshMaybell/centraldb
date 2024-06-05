"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.domain.threshold_base import ThresholdBase

class RangeThreshold(ThresholdBase):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: str = ...,
        min: Incomplete | None = ...,
        max: Incomplete | None = ...,
        within: Incomplete | None = ...,
        level: Incomplete | None = ...,
        all_values: Incomplete | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def min(self): ...
    @min.setter
    def min(self, min) -> None: ...
    @property
    def max(self): ...
    @max.setter
    def max(self, max) -> None: ...
    @property
    def within(self): ...
    @within.setter
    def within(self, within) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
