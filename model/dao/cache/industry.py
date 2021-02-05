from model.entities.industry import SystemCosts


class UniverseCache:
    def __init__(self, cache, api):
        self.cache = cache
        self.api = api

    def load_cost_indices(self):
        base_key = "costs_indices"
        ids_str = self.cache[base_key + ".all.id"]
        if ids_str is not None:
            ids = ids_str.split(";")
            costs = []
            for id_ in ids:
                cost_base_key = base_key + f".{id_}"
                costs.append(SystemCosts(self.cache[cost_base_key + ".id"],
                                         self.cache[cost_base_key + ".manufacturing"],
                                         self.cache[cost_base_key + ".researching_time_efficiency"],
                                         self.cache[cost_base_key + ".researching_material_efficiency"],
                                         self.cache[cost_base_key + ".copying"],
                                         self.cache[cost_base_key + ".copying"],
                                         self.cache[cost_base_key + ".reaction"]))
        costs = self.api.load_cost_indices()
        ids = []
        for cost in costs:
            ids.append(cost.system_id)
            cost_base_key = base_key + f".{cost.system_id}"
            self.cache[cost_base_key + ".id"] = cost.system_id
            self.cache[cost_base_key + ".manufacturing"] = cost.manufacturing
            self.cache[cost_base_key + ".researching_time_efficiency"] = cost.researching_time_efficiency
            self.cache[cost_base_key + ".researching_material_efficiency"] = cost.researching_material_efficiency
            self.cache[cost_base_key + ".copying"] = cost.copying
            self.cache[cost_base_key + ".copying"] = cost.invention
            self.cache[cost_base_key + ".reaction"] = cost.reaction
        ids_str = ";".join(ids)
        self.cache[base_key + ".all.id"] = ids_str
        return costs
