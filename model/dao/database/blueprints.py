from model.entities.assets import Manufacturing, Material, Product


class BlueprintsDB:
    def __init__(self, db):
        self.__db = db

    def save_all_static(self, static_blueprints):
        for bp in static_blueprints:
            self.__save_static(bp)

    def __save_static(self, static_blueprints):
        cursor = self.__db.cursor()
        for mat in static_blueprints.manufacturing.materials:
            cursor.execute("INSERT INTO manufacturing_materials (blueprint_id, type_id, quantity) VALUES (?, ?, ?)",
                           (static_blueprints.id, mat.type_id, mat.quantity))
        for prod in static_blueprints.manufacturing.products:
            cursor.execute("INSERT INTO manufacturing_products (blueprint_id, type_id, quantity) VALUES (?, ?, ?)",
                           (static_blueprints.id, prod.type_id, prod.quantity))
        cursor.execute("INSERT INTO blueprint_details (id, manufacturing_time) VALUES (?, ?)",
                       (static_blueprints.id, static_blueprints.manufacturing.time))

        self.__db.commit()
        cursor.close()

    def load_manufacturing(self, blueprint_id: int):
        cursor = self.__db.cursor()

        details_result = cursor.execute("SELECT manufacturing_time FROM blueprint_details WHERE id = ?",
                                        (blueprint_id,)).fetchone()
        if details_result is None:
            return None
        materials_result = cursor.execute(
            "SELECT type_id, quantity FROM manufacturing_materials WHERE blueprint_id = ?",
            (blueprint_id,)).fetchall()
        materials = []
        for mat_res in materials_result:
            materials.append(Material(mat_res[0], mat_res[1]))
        products_result = cursor.execute("SELECT type_id, quantity FROM manufacturing_products WHERE blueprint_id = ?",
                                         (blueprint_id,)).fetchall()
        products = []
        for prod_res in products_result:
            products.append(Product(prod_res[0], prod_res[1]))
        manufacturing = Manufacturing(details_result[0], materials, products)
        cursor.close()
        return manufacturing
