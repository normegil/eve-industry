class Group:
    def __init__(self, character_id=None, name=None, category=None):
        self.id = character_id
        self.name = name
        self.category = category
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def asset(self, searched_asset_id):
        for asset in self.assets:
            if searched_asset_id == asset.id:
                return asset
        return None
