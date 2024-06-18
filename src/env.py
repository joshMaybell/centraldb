"""Module providing global constants from the environment."""

import os

DBDIR = os.environ.get("DBDIR", os.path.expanduser("~/.centraldb"))
DB = "sqlite:///" + os.path.join(DBDIR, "tracking.db")
LOCAL_IDB_URL = os.environ.get("LOCAL_IDB_URL", "http://localhost:8086")
