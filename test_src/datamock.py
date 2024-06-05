# pylint: disable=invalid-name
import builtins
import datetime
import enum
import os
import random
import string
import sys
import time
import types
from typing import Any, Type, Union
import typing

import influxdb_client.client.influxdb_client
import influxdb_client.client.write.point
import influxdb_client.client.write_api
import pydantic
import urllib3.exceptions

import models


def get_random_of_type(target_type: Type[Any]) -> Any:
    """Return a random value of type: target_type.

    Supported types are:
        str,
        int,
        float,
        bool
        Enum

    Unions of supported types are also allowed.

    In the case of a union of types, a random valid type in the union is used.

    Args:
        target_type:
            The type of the random value to return.

    """
    match target_type:
        case builtins.str:
            # Generate a random string of length 6.
            return "".join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                for _ in range(6)
            )
        case builtins.int:
            return random.randint(0, 100)

        case builtins.float:
            return random.random() * 100

        case builtins.bool:
            return random.random() > 0.5

        # Case for enum types
        case _ if isinstance(target_type, enum.EnumMeta):
            # Return a random value from the enum type
            enum_member_list: list[enum.Enum] = list(target_type)
            return random.choice(enum_member_list)

        # Case for union types
        case _ if isinstance(target_type, types.UnionType):
            valid_types: list[type] = []
            # Iterate through types in the union
            for type_ in typing.get_args(target_type):
                try:
                    # get a random value for each supported type
                    valid_types.append(get_random_of_type(type_))
                except TypeError:
                    pass
            # If there were no valid types in the union, the union is not supported
            if not valid_types:
                raise TypeError("Unsupported Type: ", target_type)

            # Return a random value of a random type from the union.
            return random.choice(valid_types)
        case _:
            raise TypeError("Unsupported Type: ", target_type)


def random_model(model: Type[pydantic.BaseModel]):
    """Populate fields with example values.

    Parses the fields of a pydantic model and generates random values for
    each field.

    Excludes the 'name' field, if it exists.

    Args:
        model: The BaseModel metaclass to generate values for.

    Returns:
        dict[str, Any]: A dictionary mapping the field names to their random values.
    """

    result: dict[str, Any] = {}

    for name, field in model.model_fields.items():
        if name != "name":
            if field.annotation is not None:
                result[name] = get_random_of_type(field.annotation)

    return dict(result)


def ensure_bucket_exists(bucket: str, client: influxdb_client.InfluxDBClient):
    """Ensure that the bucket `bucket` exists in `client`'s database.

    If `bucket` is not found, it is created.

    Returns:
        (bool): True if the bucket was successfully created, False otherwise.
    """
    buckets_api = client.buckets_api()

    # Give the db 5 seconds to boot, if it's not already running.
    for _ in range(5):
        try:
            if buckets_api.find_bucket_by_name(bucket) is None:
                buckets_api.create_bucket(bucket_name=bucket)
            return True
        except urllib3.exceptions.HTTPError:
            time.sleep(1)

    return False


EventData = Union[str, bytes, dict[str, "EventData"], list["EventData"]]


def _recursive_cast(data: dict[str, Any] | list[Any] | tuple[Any] | Any):
    out: list[EventData] | dict[str, EventData]
    if isinstance(data, dict):
        out = {}
        for name, value in data.items():
            if isinstance(value, (dict, list, tuple)):
                out[name] = _recursive_cast(value)  # type: ignore

            else:
                out[name] = str(value)

    elif hasattr(data, "__iter__"):
        out = []
        for value in data:
            if isinstance(value, (dict, list, tuple)):
                out.append(_recursive_cast(value))  # type: ignore

            else:
                out.append(str(value))
    else:
        return str(data)

    return out


def main():
    """Generate and log random system data.

    Generates random data for a realistic set of devices, and logs the data to
    influxdb on an interval.

    The default logging interval is 10 seconds, but this can be adjusted by setting
    the 'INTERVAL' environment variable.

    The default influxdb bucket is 'datadb', but this can be changed by setting
    the "BUCKET" environment variable.

    The default influxdb url is 'http://localhost:8086', but this can be changed by
    setting the "URL" environment variable.

    The default influxdb org is 'maybell', but this can be changed by setting the
    "ORG" environment variable.

    The default influxdb username is 'admin', but this can be changed by setting
    the "USERNAME" environment variable.

    The default influxdb password is 'password', but this can be changed by
    setting the "PASSWORD" environment variable.
    """

    # Collect configurable parameters from the environment
    try:
        interval = float(os.environ.get("INTERVAL", 10))

    # The "INTERVAL" variable must be numeric.
    except ValueError:
        print("Invalid interval. Value must be numeric.")
        sys.exit(1)

    url = os.environ.get("URL", "http://localhost:8086")
    org = os.environ.get("ORG", "maybell")
    bucket = os.environ.get("BUCKET", "datadb")
    username = os.environ.get("USERNAME", "admin")
    password = os.environ.get("PASSWORD", "password")

    # Create the influxdb client used to write the random data points.
    client = influxdb_client.client.influxdb_client.InfluxDBClient(
        url=url, org=org, username=username, password=password
    )

    write_api = client.write_api(
        write_options=influxdb_client.client.write_api.SYNCHRONOUS
    )

    # Make sure our target influxdb bucket exists.
    ensure_bucket_exists(bucket, client)

    # Construct a set of devices to use as a mock system.
    mocks: dict[Type[models.Model], list[str]] = {}

    mocks[models.Compressor] = ["cp1", "cp2"]
    mocks[models.Ecodry] = ["pm2"]
    mocks[models.Flow] = ["f1"]
    mocks[models.Heater] = ["sample", "still", "warmup"]
    mocks[models.Inverter] = ["inv1"]
    mocks[models.Pressure] = [f"p{ii}" for ii in range(1, 9)]
    mocks[models.Pump] = ["pm4", "pm5"]
    mocks[models.Thermometer] = ["prp", "rgp", "cfp", "icp", "stp", "mxp"]
    mocks[models.Turbo] = ["pm1", "pm3"]
    mocks[models.Valve] = [f"v{ii}" for ii in range(1, 27)]

    # Write random data to the database forever.
    print("Starting Datamock...", flush=True)
    while True:
        all_values: dict[str, dict[str, Any]] = {}
        points: list[influxdb_client.client.write.point.Point] = []
        current_time = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        # pylint: disable=protected-access
        for type_, list_ in mocks.items():
            for name in list_:
                new_model = type_(name=name, **random_model(type_))
                if new_model._type not in all_values:
                    all_values[new_model._type] = {
                        new_model.name: new_model.model_dump()
                    }
                else:
                    all_values[new_model._type][new_model.name] = new_model.model_dump()
                points.append(new_model.as_point(time=current_time))

        with write_api:
            write_api.write(bucket=bucket, record=points)

        time.sleep(interval)


if __name__ == "__main__":
    main()
