class Character:
    def __init__(self, character_id=None, name=None, assets=None):
        if assets is None:
            assets = {}
        self.id = character_id
        self.name = name
        self.assets = assets
