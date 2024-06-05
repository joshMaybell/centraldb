"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

class ReplicationCreationRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        name: Incomplete | None = ...,
        description: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        remote_id: Incomplete | None = ...,
        local_bucket_id: Incomplete | None = ...,
        remote_bucket_id: Incomplete | None = ...,
        remote_bucket_name: str | None = ...,
        max_queue_size_bytes: int = ...,
        drop_non_retryable_data: bool = ...,
        max_age_seconds: int = ...,
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def remote_id(self): ...
    @remote_id.setter
    def remote_id(self, remote_id) -> None: ...
    @property
    def local_bucket_id(self): ...
    @local_bucket_id.setter
    def local_bucket_id(self, local_bucket_id) -> None: ...
    @property
    def remote_bucket_id(self): ...
    @remote_bucket_id.setter
    def remote_bucket_id(self, remote_bucket_id) -> None: ...

    remote_bucket_name: str | None
    @property
    def max_queue_size_bytes(self): ...
    @max_queue_size_bytes.setter
    def max_queue_size_bytes(self, max_queue_size_bytes) -> None: ...
    @property
    def drop_non_retryable_data(self): ...
    @drop_non_retryable_data.setter
    def drop_non_retryable_data(self, drop_non_retryable_data) -> None: ...

    max_age_seconds: int
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...