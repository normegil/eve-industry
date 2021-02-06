from .asset import Asset, IndividualAsset


class Blueprint(Asset):
    def __init__(self, type_id):
        Asset.__init__(self, type_id)
        self.manufacturing = None


class IndividualBlueprint(IndividualAsset):
    def __init__(self, asset_id, location, quantity, runs, material_efficiency, time_efficiency):
        IndividualAsset.__init__(self, asset_id, location)
        self.quantity = quantity
        self.runs = runs
        self.material_efficiency = material_efficiency
        self.time_efficiency = time_efficiency


class Manufacturing:
    def __init__(self, time, materials, products):
        self.time = time
        self.materials = materials
        self.products = products


class Material:
    def __init__(self, type_id, quantity):
        self.type_id = type_id
        self.quantity = quantity


class Product:
    def __init__(self, type_id, quantity):
        self.type_id = type_id
        self.quantity = quantity
