"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class TemplateSummary:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        sources: Incomplete | None = ...,
        stack_id: Incomplete | None = ...,
        summary: Incomplete | None = ...,
        diff: Incomplete | None = ...,
        errors: Incomplete | None = ...,
    ) -> None: ...
    @property
    def sources(self): ...
    @sources.setter
    def sources(self, sources) -> None: ...
    @property
    def stack_id(self): ...
    @stack_id.setter
    def stack_id(self, stack_id) -> None: ...
    @property
    def summary(self): ...
    @summary.setter
    def summary(self, summary) -> None: ...
    @property
    def diff(self): ...
    @diff.setter
    def diff(self, diff) -> None: ...
    @property
    def errors(self): ...
    @errors.setter
    def errors(self, errors) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
