"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class Stack:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        events: Incomplete | None = ...,
    ) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def created_at(self): ...
    @created_at.setter
    def created_at(self, created_at) -> None: ...
    @property
    def events(self): ...
    @events.setter
    def events(self, events) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
