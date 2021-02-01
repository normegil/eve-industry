from sqlite3 import Cursor


def upgrade_to_v1(cursor: Cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS asset_minimum_stock ("
        "asset_id INTEGER PRIMARY KEY, "
        "minimum_stock INTEGER"
        ")")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS warehouse_asset_displayed ("
        "group_id INTEGER PRIMARY KEY"
        ")")
    cursor.execute(
        "INSERT INTO warehouse_asset_displayed (group_id) VALUES (18)")
