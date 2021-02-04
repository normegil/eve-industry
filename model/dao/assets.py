from model.dao.database import AssetsDB
from model.dao.eveapi import AssetsAPI


class AssetsDAO:
    def __init__(self, assets_db: AssetsDB, assets_api: AssetsAPI):
        self.assets_api = assets_api
        self.assets_db = assets_db

    def owned(self, character_id):
        return self.assets_api.owned(character_id)

    def load_minimum_stocks(self, categories: []):
        for category in categories:
            for group in category.groups:
                for asset in group.assets:
                    asset.minimum_stock = self.assets_db.load_minimum_stock(asset.id)

    def save_minimum_stock(self, asset_id: int, minimum_stock: int):
        self.assets_db.save_minimum_stock(asset_id, minimum_stock)
