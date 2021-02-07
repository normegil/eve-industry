from model.entities.industry import SystemCosts


class IndustryCache:
    def __init__(self, cache, api):
        self.cache = cache
        self.api = api

    def load_cost_indices(self):
        return self.api.load_cost_indices()

    def load_system_cost_indices(self, system_id):
        base_key = f"costs_indices.{system_id}"
        cost_system_id = self.cache[base_key + ".id"]
        if cost_system_id is not None:
            manufacturing = self.cache[base_key + ".manufacturing"]
            time_efficiency = self.cache[base_key + ".researching_time_efficiency"]
            material_efficiency = self.cache[base_key + ".researching_material_efficiency"]
            copying = self.cache[base_key + ".copying"]
            invention = self.cache[base_key + ".invention"]
            reaction = self.cache[base_key + ".reaction"]
            return SystemCosts(cost_system_id, manufacturing, time_efficiency, material_efficiency, copying, invention,
                               reaction)
        costs = self.load_cost_indices()
        cost = find_cost(costs, system_id)
        cost_base_key = f"costs_indices.{cost.system_id}"
        self.cache[cost_base_key + ".id"] = cost.system_id
        self.cache[cost_base_key + ".manufacturing"] = cost.manufacturing
        self.cache[cost_base_key + ".researching_time_efficiency"] = cost.researching_time_efficiency
        self.cache[cost_base_key + ".researching_material_efficiency"] = cost.researching_material_efficiency
        self.cache[cost_base_key + ".copying"] = cost.copying
        self.cache[cost_base_key + ".invention"] = cost.invention
        self.cache[cost_base_key + ".reaction"] = cost.reaction
        return cost


def find_cost(costs, system_id):
    for cost in costs:
        if cost.system_id == system_id:
            return cost
    return None
