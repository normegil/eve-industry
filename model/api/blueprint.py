from model.entities.assets import Blueprint, IndividualBlueprint


class BlueprintModelAPI:
    def __init__(self, warehouse):
        self.__warehouse = warehouse

    def total_price(self, individual_blueprint: IndividualBlueprint):
        blueprint: Blueprint = individual_blueprint.parent
        return self.materials_prices(blueprint.manufacturing.materials)

    def materials_prices(self, materials):
        total_materials_cost = 0
        for material in materials:
            asset = self.__warehouse.asset(material.type_id)
            total_materials_cost += material.quantity * asset.average_price_per_unit
        return total_materials_cost
