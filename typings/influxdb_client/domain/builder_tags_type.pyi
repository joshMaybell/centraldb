"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class BuilderTagsType:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        key: Incomplete | None = ...,
        values: Incomplete | None = ...,
        aggregate_function_type: Incomplete | None = ...,
    ) -> None: ...
    @property
    def key(self): ...
    @key.setter
    def key(self, key) -> None: ...
    @property
    def values(self): ...
    @values.setter
    def values(self, values) -> None: ...
    @property
    def aggregate_function_type(self): ...
    @aggregate_function_type.setter
    def aggregate_function_type(self, aggregate_function_type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
