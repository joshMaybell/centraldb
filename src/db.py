"""Module providing utilities for tracking the status of synced databases.

This module uses sqlalchemy to manage a database of synced databases.
The primary objective is to track synced databases by name, and store
the timestamp of the previous sync for that database.
"""

import time

import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.orm

import env

_DEFAULT_ENGINE = sqlalchemy.create_engine(env.DB)


class _DbState(sqlalchemy.orm.declarative_base()):
    __tablename__ = "db_state"

    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True)

    db_name: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(
        unique=True, index=True, nullable=False
    )

    sync_time: sqlalchemy.orm.Mapped[float] = sqlalchemy.orm.mapped_column(
        nullable=False
    )


def init_engine(
    engine: sqlalchemy.Engine | None = None,
):
    """Create the tables required for the tracking system to function.

    Tables that already exist are not recreated.

    Returns:
        (bool): True is the metadata was successfully created, False otherwise.
    """

    if engine is None:
        engine = _DEFAULT_ENGINE

    # Give the db 5 seconds to boot, if it's not already running.
    exc: sqlalchemy.exc.SQLAlchemyError | None = None
    for _ in range(5):
        try:
            _DbState.metadata.create_all(engine)
            return True
        except sqlalchemy.exc.SQLAlchemyError as e:
            time.sleep(1)
            exc = e

    if exc is not None:
        raise exc

    return False


def update(
    db_name: str,
    sync_time: float | None = None,
    engine: sqlalchemy.Engine | None = None,
):
    """Update the sync time of a tracked database.

    If the requested database name does not exist in the tracking system,
    that database name is added.

    Args:
        db_name (str): The name of the tracked database to update.
        sync_time (float | None): The timestamp to use when updating the
        tracked database. If None (default), the current time is used.
        engine (Engine): The SQLAlchemy engine used to connect to the
        tracking database. If None (default), the default engine is used.
    """

    if engine is None:
        engine = _DEFAULT_ENGINE

    if sync_time is None:
        sync_time = time.time()

    with sqlalchemy.orm.Session(engine, expire_on_commit=False) as session:
        db = session.query(_DbState).filter(_DbState.db_name == db_name).first()

        if db is None:
            db = _DbState()
            db.db_name = db_name
            db.sync_time = sync_time
            session.add(db)
        else:
            db.sync_time = sync_time

        session.commit()


def get_sync_time(db_name: str, engine: sqlalchemy.Engine | None = None):
    """Return the timestamp when the tracked database was previously synced.

    If the requested database name does not exist in the tracking system,
    returns 0.

    Args:
        db_name (str): The name of the tracked database to update.
        engine (Engine): The SQLAlchemy engine used to connect to the
        tracking database. If None (default), the default engine is used.
    """
    if engine is None:
        engine = _DEFAULT_ENGINE

    with sqlalchemy.orm.Session(engine, expire_on_commit=False) as session:
        db = session.query(_DbState).filter(_DbState.db_name == db_name).first()

        if db is None:
            return 0

        return db.sync_time
