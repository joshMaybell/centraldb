"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class TemplateSummaryDiffTelegrafConfigs:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        kind: Incomplete | None = ...,
        state_status: Incomplete | None = ...,
        id: Incomplete | None = ...,
        template_meta_name: Incomplete | None = ...,
        new: Incomplete | None = ...,
        old: Incomplete | None = ...,
    ) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def state_status(self): ...
    @state_status.setter
    def state_status(self, state_status) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def template_meta_name(self): ...
    @template_meta_name.setter
    def template_meta_name(self, template_meta_name) -> None: ...
    @property
    def new(self): ...
    @new.setter
    def new(self, new) -> None: ...
    @property
    def old(self): ...
    @old.setter
    def old(self, old) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
