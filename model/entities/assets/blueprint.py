from .assets import Assets, AssetLocation


class Blueprint(Assets):
    def __init__(self, type_id):
        Assets.__init__(self, type_id)


class BlueprintLocation(AssetLocation):
    def __init__(self, asset_id, location_id, location_type, quantity, runs, material_efficiency, time_efficiency):
        AssetLocation.__init__(self, asset_id, location_id, location_type)
        self.quantity = quantity
        self.runs = runs
        self.material_efficiency = material_efficiency
        self.time_efficiency = time_efficiency
