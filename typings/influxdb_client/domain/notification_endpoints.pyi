"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class NotificationEndpoints:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        notification_endpoints: Incomplete | None = ...,
        links: Incomplete | None = ...,
    ) -> None: ...
    @property
    def notification_endpoints(self): ...
    @notification_endpoints.setter
    def notification_endpoints(self, notification_endpoints) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
