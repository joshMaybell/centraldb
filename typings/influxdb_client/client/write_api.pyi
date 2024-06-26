"""
This type stub file was generated by pyright.
"""

from _typeshed import DataclassInstance, Incomplete
from collections.abc import Iterable
from enum import Enum
import logging
from types import TracebackType
from typing import Any, NamedTuple
from typing_extensions import Self, TypeAlias

from influxdb_client.client._base import _BaseWriteApi
from influxdb_client.client.write.point import Point
from influxdb_client.domain.write_precision import _WritePrecision
from reactivex import Observable

_DataClass: TypeAlias = DataclassInstance
_NamedTuple: TypeAlias = NamedTuple
_Observable: TypeAlias = Observable[Any]
logger: logging.Logger

class WriteType(Enum):
    batching: int
    asynchronous: int
    synchronous: int
    ...

class WriteOptions:
    write_type: WriteType
    batch_size: int
    flush_interval: int
    jitter_interval: int
    retry_interval: int
    max_retries: int
    max_retry_delay: int
    max_retry_time: int
    exponential_base: int
    write_scheduler: Incomplete
    max_close_wait: int
    def __init__(
        self,
        write_type: WriteType = ...,
        batch_size: int = ...,
        flush_interval: int = ...,
        jitter_interval: int = ...,
        retry_interval: int = ...,
        max_retries: int = ...,
        max_retry_delay: int = ...,
        max_retry_time: int = ...,
        exponential_base: int = ...,
        max_close_wait: int = ...,
        write_scheduler=...,
    ) -> None: ...
    def to_retry_strategy(self, **kwargs): ...

SYNCHRONOUS: Incomplete
ASYNCHRONOUS: Incomplete

class PointSettings:
    defaultTags: Incomplete
    def __init__(self, **default_tags) -> None: ...
    def add_default_tag(self, key, value) -> None: ...

class _BatchItemKey:
    bucket: Incomplete
    org: Incomplete
    precision: Incomplete
    def __init__(self, bucket, org, precision=...) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, o: object) -> bool: ...

class _BatchItem:
    key: Incomplete
    data: Incomplete
    size: Incomplete
    def __init__(self, key: _BatchItemKey, data, size: int = ...) -> None: ...
    def to_key_tuple(self) -> tuple[str, str, str]: ...

class _BatchResponse:
    data: Incomplete
    exception: Incomplete
    def __init__(self, data: _BatchItem, exception: Exception | None = ...) -> None: ...

class WriteApi(_BaseWriteApi):
    def __init__(
        self,
        influxdb_client,
        write_options: WriteOptions = ...,
        point_settings: PointSettings = ...,
        **kwargs
    ) -> None: ...
    def write(
        self,
        bucket: str,
        org: str | None = ...,
        record: str
        | Iterable[str]
        | Point
        | Iterable[Point]
        | dict[Incomplete, Incomplete]
        | Iterable[dict[Incomplete, Incomplete]]
        | bytes
        | Iterable[bytes]
        | _Observable
        | _NamedTuple
        | Iterable[_NamedTuple]
        | _DataClass
        | Iterable[_DataClass] = ...,
        write_precision: _WritePrecision = ...,
        **kwargs: Any
    ) -> Any: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def __del__(self) -> None: ...
