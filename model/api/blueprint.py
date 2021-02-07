import logging

from model.entities.assets import Blueprint, IndividualBlueprint


class BlueprintModelAPI:
    def __init__(self, warehouse):
        self.__warehouse = warehouse

    def total_price(self, individual_blueprint: IndividualBlueprint, region_id):
        logging.info(f"Computing blueprint costs: {individual_blueprint.asset_id} - {region_id}")
        blueprint: Blueprint = individual_blueprint.parent
        return self.materials_prices(blueprint.manufacturing.materials, region_id)

    def materials_prices(self, materials, region_id):
        high_total_materials_cost = 0
        low_total_materials_cost = 0
        for material in materials:
            asset = self.__warehouse.asset(material.type_id)
            if material.quantity < asset.quantity:
                material_price = material.quantity * asset.average_price_per_unit
                high_total_materials_cost += material_price
                low_total_materials_cost += material_price
                continue
            else:
                stock_cost = 0
                if asset.average_price_per_unit is not None:
                    stock_cost = asset.quantity * asset.average_price_per_unit
                low_total_materials_cost = stock_cost + (
                        material.quantity - asset.quantity) * asset.highest_regional_buy_price(region_id).price_per_unit
                high_total_materials_cost = stock_cost + (
                        material.quantity - asset.quantity) * asset.lowest_regional_sell_price(region_id).price_per_unit
        return low_total_materials_cost, high_total_materials_cost
