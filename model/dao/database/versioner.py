import logging
import time
from datetime import datetime
from sqlite3 import Connection, Cursor


class Versioner:
    def __init__(self, db: Connection, versions):
        self._db = db
        self.__versions = versions

    def upgrade(self):
        current_version = self.__load_db_version()
        for upgrade in self.__load_upgrades(current_version):
            cursor = self._db.cursor()
            logging.info(f"Upgrading to {current_version + 1}")
            upgrade(cursor)
            current_version += 1
            update_version(cursor, current_version)
            self._db.commit()
            cursor.close()
            time.sleep(1)

    def __load_db_version(self):
        cursor = self._db.cursor()
        query = cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='versions';")
        result = query.fetchone()
        count = result[0]
        if count == 0:
            return -1
        version_result = cursor.execute(
            "SELECT version FROM versions ORDER BY datetime(changed_datetime) DESC LIMIT 1;").fetchone()
        cursor.close()
        return version_result[0]

    def __load_upgrades(self, current_version):
        first_version_to_apply = current_version + 1
        if len(self.__versions) <= first_version_to_apply:
            return []
        return self.__versions[first_version_to_apply:]


def update_version(cursor: Cursor, version: int):
    cursor.execute("INSERT INTO versions (version, changed_datetime) VALUES (?, ?)", (version, datetime.now()))
