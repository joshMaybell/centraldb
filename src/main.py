"""Main module for the maybell central fridge database.

Pulls and backs up data from influxdb databases listed in the sources.yaml file.
"""

import os
import time

import influxdb_client
import influxdb_client.client.flux_table
import influxdb_client.client.write_api
import pydantic
import urllib3.exceptions
import yaml

import db
import env

YamlType = int | float | bool | str | list["YamlType"] | dict[str, "YamlType"] | None


class _DB(pydantic.BaseModel):
    """Model representing a configured database source."""

    name: str
    url: str
    token: str
    org: str
    bucket: str


def _validate_sources(sources: YamlType):
    if not isinstance(sources, dict):
        raise RuntimeError(
            "Source file has an invalid structure. The root item was "
            + f"expected to be a dict, but was instead a {type(sources)}"
        )

    if "sources" not in sources:
        raise RuntimeError(
            "Source file must have a list of sources under the key 'sources'."
        )

    source_list = sources["sources"]

    if not isinstance(source_list, list):
        raise RuntimeError(
            "sources structure in the Source file must be a list of "
            + f"db configuration objects, not {type(sources['sources'])}"
        )

    dbs: list[_DB] = []

    for source in source_list:
        if not isinstance(source, dict):
            raise RuntimeError(
                "Each source must be an db configuration object "
                + "containing a 'name' and 'url' object."
            )

        name = source.get("name")
        url = source.get("url")
        token = source.get("token")
        org = source.get("org")
        bucket = source.get("bucket")

        if not isinstance(name, str):
            raise RuntimeError(
                "Db configuration object must contain a 'name' of type string"
            )
        if not isinstance(url, str):
            raise RuntimeError(
                "Db configuration object must contain a 'url' of type string"
            )
        if not isinstance(token, str):
            raise RuntimeError(
                "Db configuration object must contain a 'token' of type string"
            )
        if not isinstance(org, str):
            raise RuntimeError(
                "Db configuration object must contain a 'org' of type string"
            )
        if not isinstance(bucket, str):
            raise RuntimeError(
                "Db configuration object must contain a 'bucket' of type string"
            )

        dbs.append(_DB(name=name, url=url, token=token, org=org, bucket=bucket))

    return dbs


def _record_to_point(record: influxdb_client.client.flux_table.FluxRecord):
    """Convert a FluxRecord into a Point."""
    point = influxdb_client.Point(record.get_measurement())

    point.time(record.get_time())
    point.field(record.get_field(), record.get_value())

    for key, value in record.values.items():
        if key not in [
            "_measurement",
            "_field",
            "_value",
            "_time",
            "result",
            "table",
            "_stop",
            "_start",
        ]:
            point = point.tag(key, value)

    return point


def _format_time(t: float):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def _query_all(
    query_api: influxdb_client.QueryApi,
    bucket: str,
    start_time: float,
    end_time: float | None = None,
):

    start_str = f"start: {_format_time(start_time)}"
    end_str = "" if end_time is None else f", stop: {_format_time(end_time)}"
    query = f"""from(bucket: "{bucket}")
                     |> range({start_str}{end_str})"""

    return query_api.query_stream(query)


def _ensure_bucket_exists(bucket: str, client: influxdb_client.InfluxDBClient):
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


def _sync_db(source: _DB, start_time: float, end_time: float | None = None):
    """Pull and backup a target db."""
    client = influxdb_client.InfluxDBClient(
        url=source.url, token=source.token, org=source.org
    )

    query_api = client.query_api()

    dest_bucket_name = source.name
    dest_client = influxdb_client.InfluxDBClient(
        url=env.LOCAL_IDB_URL, token="12345678=", org="maybell"
    )

    tables = _query_all(query_api, source.bucket, start_time, end_time)

    _ensure_bucket_exists(dest_bucket_name, dest_client)

    with dest_client.write_api(
        write_options=influxdb_client.client.write_api.SYNCHRONOUS
    ) as write_api:

        all_points_consumed = False

        while not all_points_consumed:
            points: list[influxdb_client.Point] = []

            # Consume 10000 points at a time.
            for _ in range(10000):
                try:
                    points.append(_record_to_point(next(tables)))
                except StopIteration:
                    all_points_consumed = True
                    break

            if points:
                write_api.write(bucket=dest_bucket_name, record=points)


def main():
    """Pull and backup data from configured databases."""

    os.makedirs(env.DBDIR, exist_ok=True)

    db.init_engine()

    while True:

        with open("sources.yaml", encoding="utf-8") as f:
            config: dict[str, YamlType] = yaml.safe_load(f.read())
            dbs = _validate_sources(config)
            delay = config.get("sync-rate", 600)
            if not isinstance(delay, (float, int)):
                print(
                    "CONFIG ERROR: 'sync-rate' is an invalid type. "
                    + "Expected a numeric type, but got: ",
                    type(delay),
                )
                print("Defaulting to default sync-rate: ", 600)
                delay = 600

        for d in dbs:
            t = db.get_sync_time(d.name)
            try:
                print(f"Syncing db '{d.name}...'")
                _sync_db(d, t)
                print(f"Updating sync state...")
                db.update(d.name)
                print(f"'{d.name}' finished syncing.")
            except (IOError, urllib3.exceptions.NewConnectionError) as e:
                print("FAILED TO SYNC DB:", d.name, " do to error: ", e)

            print("\n")

        print(f"Sync cycle finished. Will run again in {delay} seconds.")
        time.sleep(delay)


if __name__ == "__main__":
    main()
