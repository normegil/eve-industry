import logging
import os
import sqlite3

from model.dao.database import Versioner, BlueprintsDB
from model.dao.database.versioning.static import upgrades as static_versions
from model.dao.static import BlueprintsStatic

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if not os.path.exists("data"):
        os.mkdir("data")
    with sqlite3.connect("data/static.db") as dbconn:
        Versioner(dbconn, static_versions).upgrade()
        blueprints = BlueprintsStatic().load()
        BlueprintsDB(dbconn).save_all_static(blueprints)
