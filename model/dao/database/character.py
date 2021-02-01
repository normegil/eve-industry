from sqlite3 import Connection
import logging


class CharacterDB:
    def __init__(self, db: Connection):
        self.__db = db

    def load_asset_minimum_stock(self, asset_id: int):
        cursor = self.__db.cursor()
        result = cursor.execute("SELECT minimum_stock FROM asset_minimum_stock WHERE asset_id = ?",
                                (asset_id,)).fetchone()
        cursor.close()
        if result is None:
            return None
        return result[0]

    def save_asset_minimum_stock(self, asset_id: int, minimum_stock: int):
        cursor = self.__db.cursor()
        result = cursor.execute("SELECT COUNT(1) FROM asset_minimum_stock WHERE asset_id = ?",
                                (asset_id,)).fetchone()
        if result[0] == 0:
            cursor.execute("INSERT INTO asset_minimum_stock (asset_id, minimum_stock) VALUES (?, ?)",
                           (asset_id, minimum_stock))
        else:
            cursor.execute("UPDATE asset_minimum_stock SET minimum_stock=? WHERE asset_id=?",
                           (minimum_stock, asset_id))
        self.__db.commit()
        cursor.close()

    def load_warehouse_displayed_asset(self):
        cursor = self.__db.cursor()
        results = cursor.execute("SELECT group_id FROM warehouse_asset_displayed").fetchall()
        cursor.close()
        group_ids = []
        for result in results:
            group_ids.append(result[0])
        return group_ids

    def add_warehouse_displayed_asset(self, group_id: int):
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO warehouse_asset_displayed (group_id) VALUES (?)", (group_id, ))
        self.__db.commit()
        cursor.close()

    def remove_warehouse_displayed_asset(self, group_id: int):
        cursor = self.__db.cursor()
        cursor.execute("DELETE FROM warehouse_asset_displayed WHERE group_id = ?", (group_id,))
        self.__db.commit()
        cursor.close()
