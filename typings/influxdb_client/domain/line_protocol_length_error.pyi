"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class LineProtocolLengthError:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, code: Incomplete | None = ..., message: Incomplete | None = ...
    ) -> None: ...
    @property
    def code(self): ...
    @code.setter
    def code(self, code) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
