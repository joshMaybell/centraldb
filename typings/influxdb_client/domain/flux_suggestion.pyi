"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class FluxSuggestion:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, name: Incomplete | None = ..., params: Incomplete | None = ...
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def params(self): ...
    @params.setter
    def params(self, params) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
