"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client import Bucket

class BucketsApi:
    def __init__(self, influxdb_client) -> None: ...
    def create_bucket(
        self,
        bucket: Incomplete | None = ...,
        bucket_name: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        retention_rules: Incomplete | None = ...,
        description: Incomplete | None = ...,
        org: Incomplete | None = ...,
    ) -> Bucket: ...
    def update_bucket(self, bucket: Bucket) -> Bucket: ...
    def delete_bucket(self, bucket: Bucket) -> Bucket: ...
    def find_bucket_by_id(self, id): ...
    def find_bucket_by_name(self, bucket_name: str) -> Bucket | None: ...
    def find_buckets(self, **kwargs): ...
