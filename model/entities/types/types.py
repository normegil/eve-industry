class Type:
    def __init__(self, id_=None, name=None, description=None, volume=None, packaged_volume=None, group=None):
        self.id = id_
        self.name = name
        self.description = description
        self.volume = volume
        self.packaged_volume = packaged_volume
        self.group = group