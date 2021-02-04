from sqlite3 import Connection


class WarehouseDB:
    def __init__(self, db: Connection):
        self.__db = db

    def displayed_groups_ids(self):
        cursor = self.__db.cursor()
        results = cursor.execute("SELECT group_id FROM warehouse_asset_displayed").fetchall()
        cursor.close()
        group_ids = []
        for result in results:
            group_ids.append(result[0])
        return group_ids

    def add_displayed_groups_ids(self, group_id: int):
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO warehouse_asset_displayed (group_id) VALUES (?)", (group_id,))
        self.__db.commit()
        cursor.close()

    def remove_displayed_groups_ids(self, group_id: int):
        cursor = self.__db.cursor()
        cursor.execute("DELETE FROM warehouse_asset_displayed WHERE group_id = ?", (group_id,))
        self.__db.commit()
        cursor.close()
