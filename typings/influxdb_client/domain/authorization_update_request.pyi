"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class AuthorizationUpdateRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, status: str = ..., description: Incomplete | None = ...
    ) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
