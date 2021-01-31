from sqlite3 import Cursor


def upgrade_to_v1(cursor: Cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS asset_minimum_stock ("
        "asset_id INTEGER PRIMARY KEY, "
        "minimum_stock INTEGER"
        ")")
