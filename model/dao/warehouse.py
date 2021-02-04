class WarehouseDAO:
    def __init__(self, warehouse_db):
        self.warehouse_db = warehouse_db

    def displayed_groups_ids(self):
        return self.warehouse_db.displayed_groups_ids()

    def add_displayed_groups_ids(self, group_id: int):
        self.warehouse_db.add_displayed_groups_ids(group_id)

    def remove_displayed_groups_ids(self, group_id: int):
        self.warehouse_db.remove_displayed_groups_ids(group_id)
