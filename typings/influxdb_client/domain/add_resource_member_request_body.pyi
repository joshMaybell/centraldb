"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class AddResourceMemberRequestBody:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, id: Incomplete | None = ..., name: Incomplete | None = ...
    ) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
