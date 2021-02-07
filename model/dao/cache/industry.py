from model.entities.industry import SystemCosts


class IndustryCache:
    def __init__(self, cache, api, all_cost_indices_in_cache=False):
        self.cache = cache
        self.api = api
        self.__all_cost_indices_in_cache = all_cost_indices_in_cache

    def load_cost_indices(self):
        if not self.__all_cost_indices_in_cache:
            return self.api.load_cost_indices()
        base_key = f"costs_indices"
        ids_str = self.cache[base_key + "all.id"]
        if ids_str is not None:
            ids = ids_str.split(";")
            costs = []
            for id_ in ids:
                costs.append(self.__load_cost_indice(id_))
        indices = self.api.load_cost_indices()
        ids = []
        for i in indices:
            ids.append(i)
            self.__store_cost_indice(i)
        self.cache[base_key + "all.id"] = ";".join(str(id_) for id_ in ids)
        return indices

    def load_system_cost_indices(self, system_id):
        base_key = f"costs_indices.{system_id}"
        cost_system_id = self.cache[base_key + ".id"]
        if cost_system_id is not None:
            return self.__load_cost_indice(cost_system_id)
        costs = self.load_cost_indices()
        cost = find_cost(costs, system_id)
        self.__store_cost_indice(cost)
        return cost

    def __load_cost_indice(self, cost_system_id):
        base_key = f"costs_indices.{cost_system_id}"
        manufacturing = self.cache[base_key + ".manufacturing"]
        time_efficiency = self.cache[base_key + ".researching_time_efficiency"]
        material_efficiency = self.cache[base_key + ".researching_material_efficiency"]
        copying = self.cache[base_key + ".copying"]
        invention = self.cache[base_key + ".invention"]
        reaction = self.cache[base_key + ".reaction"]
        return SystemCosts(cost_system_id, manufacturing, time_efficiency, material_efficiency, copying, invention,
                           reaction)

    def __store_cost_indice(self, cost):
        cost_base_key = f"costs_indices.{cost.system_id}"
        self.cache[cost_base_key + ".id"] = cost.system_id
        self.cache[cost_base_key + ".manufacturing"] = cost.manufacturing
        self.cache[cost_base_key + ".researching_time_efficiency"] = cost.researching_time_efficiency
        self.cache[cost_base_key + ".researching_material_efficiency"] = cost.researching_material_efficiency
        self.cache[cost_base_key + ".copying"] = cost.copying
        self.cache[cost_base_key + ".invention"] = cost.invention
        self.cache[cost_base_key + ".reaction"] = cost.reaction


def find_cost(costs, system_id):
    for cost in costs:
        if cost.system_id == system_id:
            return cost
    return None
