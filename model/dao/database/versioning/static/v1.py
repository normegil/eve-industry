from sqlite3 import Cursor


def upgrade_to_v1(cursor: Cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS blueprint_details ("
        "id INTEGER PRIMARY KEY, "
        "manufacturing_time INTEGER"
        ")")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS manufacturing_materials ("
        "blueprint_id INTEGER, "
        "type_id INTEGER, "
        "quantity INTEGER, "
        "PRIMARY KEY (blueprint_id, type_id)"
        ")")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS manufacturing_products ("
        "blueprint_id INTEGER, "
        "type_id INTEGER, "
        "quantity INTEGER, "
        "PRIMARY KEY (blueprint_id, type_id)"
        ")")
