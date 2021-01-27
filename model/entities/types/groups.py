class Group:
    def __init__(self, character_id=None, name=None, category=None):
        self.id = character_id
        self.name = name
        self.category = category
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def search_or_add_asset(self, searched_asset):
        for asset in self.assets:
            if searched_asset.id == asset.id:
                return asset
        self.assets.append(searched_asset)
        return searched_asset
