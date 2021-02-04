from sqlite3 import Connection


class AssetsDB:
    def __init__(self, db: Connection):
        self.__db = db

    def load_minimum_stock(self, asset_id: int):
        cursor = self.__db.cursor()
        result = cursor.execute("SELECT minimum_stock FROM asset_minimum_stock WHERE asset_id = ?",
                                (asset_id,)).fetchone()
        cursor.close()
        if result is None:
            return None
        return result[0]

    def save_minimum_stock(self, asset_id: int, minimum_stock: int):
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
