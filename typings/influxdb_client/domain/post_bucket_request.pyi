"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class PostBucketRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        org_id: Incomplete | None = ...,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        rp: str = ...,
        retention_rules: Incomplete | None = ...,
        schema_type: Incomplete | None = ...,
    ) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...

    rp: str
    @property
    def retention_rules(self): ...
    @retention_rules.setter
    def retention_rules(self, retention_rules) -> None: ...
    @property
    def schema_type(self): ...
    @schema_type.setter
    def schema_type(self, schema_type) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
