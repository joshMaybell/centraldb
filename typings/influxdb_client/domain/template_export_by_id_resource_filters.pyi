"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class TemplateExportByIDResourceFilters:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        by_label: Incomplete | None = ...,
        by_resource_kind: Incomplete | None = ...,
    ) -> None: ...
    @property
    def by_label(self): ...
    @by_label.setter
    def by_label(self, by_label) -> None: ...
    @property
    def by_resource_kind(self): ...
    @by_resource_kind.setter
    def by_resource_kind(self, by_resource_kind) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
