"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class Users:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, links: Incomplete | None = ..., users: Incomplete | None = ...
    ) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    @property
    def users(self): ...
    @users.setter
    def users(self, users) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...