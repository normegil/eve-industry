import yaml

from model.entities.assets import Material, Product, Manufacturing


class BlueprintsStatic:
    def load(self):
        with open("data/static/blueprints.yaml", "r") as file:
            loaded_data = yaml.safe_load(file)
            blueprints = []
            for bp in loaded_data:
                blueprint = StaticBlueprint(bp)
                bp_data = loaded_data[bp]
                bp_activities = bp_data["activities"]
                if hasattr(bp_activities, "manufacturing"):
                    bp_manufacturing = bp_activities["manufacturing"]
                    materials = []
                    for bp_mat in bp_manufacturing["materials"]:
                        material = Material(bp_mat["typeID"], bp_mat["quantity"])
                        materials.append(material)
                    products = []
                    for bp_prod in bp_manufacturing["products"]:
                        product = Product(bp_prod["typeID"], bp_prod["quantity"])
                        products.append(product)

                    blueprint.manufacturing = Manufacturing(bp_manufacturing["time"], materials, products)
                    blueprints.append(blueprint)
            return blueprints


class StaticBlueprint:
    def __init__(self, type_id):
        self.id = type_id
        self.manufacturing = None
