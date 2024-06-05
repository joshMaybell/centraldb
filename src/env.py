"""Module providing global constants from the environment."""

import os

DBDIR = os.environ.get("DBDIR", os.path.expanduser("~/.centraldb"))
DB = "sqlite:///" + os.path.join(DBDIR, "tracking.db")
