"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class Permission:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, action: Incomplete | None = ..., resource: Incomplete | None = ...
    ) -> None: ...
    @property
    def action(self): ...
    @action.setter
    def action(self, action) -> None: ...
    @property
    def resource(self): ...
    @resource.setter
    def resource(self, resource) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
