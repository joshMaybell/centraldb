"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class TemplateApplyTemplate:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        content_type: Incomplete | None = ...,
        sources: Incomplete | None = ...,
        contents: Incomplete | None = ...,
    ) -> None: ...
    @property
    def content_type(self): ...
    @content_type.setter
    def content_type(self, content_type) -> None: ...
    @property
    def sources(self): ...
    @sources.setter
    def sources(self, sources) -> None: ...
    @property
    def contents(self): ...
    @contents.setter
    def contents(self, contents) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
