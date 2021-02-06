from sqlite3 import Cursor


def upgrade_to_v0(cursor: Cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS versions ("
        "id INTEGER PRIMARY KEY, "
        "version INTEGER, "
        "changed_datetime TEXT"
        ")")
