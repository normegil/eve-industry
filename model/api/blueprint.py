import math

from cfg import market
from model.entities.assets import Blueprint, IndividualBlueprint


class BlueprintModelAPI:
    def __init__(self, warehouse, universe_dao):
        self.__warehouse = warehouse
        self.__universe_dao = universe_dao

    def total_price(self, individual_blueprint: IndividualBlueprint, system_id):
        blueprint: Blueprint = individual_blueprint.parent
        system = self.__universe_dao.load_system(system_id)
        low_price, high_price = self.materials_prices(blueprint.manufacturing.materials, system.constellation.region_id,
                                                      individual_blueprint.material_efficiency)
        fee = self.job_fee(blueprint.manufacturing.materials, system)
        installation_cost = fee + (fee * market.fee / 100)
        low_price += installation_cost
        high_price += installation_cost
        return low_price + (low_price * market.fee / 100), high_price + (high_price * market.fee / 100)

    def job_fee(self, materials, system):
        base_job_cost = 0
        for material in materials:
            asset = self.__warehouse.asset(material.type_id)
            base_job_cost += material.quantity * asset.adjusted_price
        return base_job_cost * system.manufacturing

    def materials_prices(self, materials, region_id, material_efficiency):
        high_total_materials_cost = 0
        low_total_materials_cost = 0
        for material in materials:
            asset = self.__warehouse.asset(material.type_id)
            required_quantity = math.ceil(material.quantity - (material.quantity * material_efficiency / 100))
            if required_quantity < asset.quantity:
                material_price = required_quantity * asset.average_price_per_unit
                high_total_materials_cost += material_price
                low_total_materials_cost += material_price
                continue
            else:
                stock_cost = 0
                if asset.average_price_per_unit is not None:
                    stock_cost = asset.quantity * asset.average_price_per_unit
                highest_region_buy = asset.highest_regional_buy_price(region_id)
                low_total_materials_cost += stock_cost + (
                        required_quantity - asset.quantity) * highest_region_buy.price_per_unit
                lowest_sell_order = asset.lowest_regional_sell_price(region_id)
                high_total_materials_cost += stock_cost + (
                        required_quantity - asset.quantity) * lowest_sell_order.price_per_unit
        return low_total_materials_cost, high_total_materials_cost
