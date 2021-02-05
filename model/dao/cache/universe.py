from model.entities import Race
from model.entities.locations import Region, Constellation, Station, System, Structure
from model.entities.types import Type, Group, Category


class UniverseCache:
    def __init__(self, cache, api):
        self.cache = cache
        self.api = api

    def load_region(self, region_id):
        base_key = f"region.{region_id}"
        id_ = self.cache[base_key + ".id"]
        if id_ is not None:
            name = self.cache[base_key + ".name"]
            description = self.cache[base_key + ".description"]
            return Region(int(id_), name, description)

        region = self.api.load_region(region_id)
        self.cache[base_key + ".id"] = region.id
        self.cache[base_key + ".name"] = region.name
        self.cache[base_key + ".description"] = region.description
        return region

    def load_constellation(self, constellation_id):
        base_key = f"constellation.{constellation_id}"
        id_ = self.cache[base_key + ".id"]
        if id_ is not None:
            name = self.cache[base_key + ".name"]
            region_id = self.cache[base_key + ".region_id"]
            c = Constellation(int(id_), name)
            c.region_id = region_id
            return c

        constellation = self.api.load_constellation(constellation_id)
        self.cache[base_key + ".id"] = constellation.id
        self.cache[base_key + ".name"] = constellation.name
        self.cache[base_key + ".region_id"] = constellation.region_id
        return constellation

    def load_system(self, system_id):
        base_key = f"system.{system_id}"
        id_ = self.cache[base_key + ".id"]
        if id_ is not None:
            name = self.cache[base_key + ".name"]
            constellation_id = self.cache[base_key + ".constellation_id"]
            s = System(int(id_), name)
            s.constellation_id = constellation_id
            return s

        system = self.api.load_system(system_id)
        self.cache[base_key + ".id"] = system.id
        self.cache[base_key + ".name"] = system.name
        self.cache[base_key + ".constellation_id"] = system.constellation_id
        return system

    def load_races(self):
        races = self.api.load_races()
        for race in races:
            self.cache[f"race.{race.id}.id"] = race.id
            self.cache[f"race.{race.id}.name"] = race.name
            self.cache[f"race.{race.id}.description"] = race.description
        return races

    def load_race(self, race_id):
        id_ = self.cache[f"race.{race_id}.id"]
        if id_ is not None:
            name = self.cache[f"race.{race_id}.name"]
            description = self.cache[f"race.{race_id}.description"]
            return Race(int(id_), name, description)

        races = self.load_races()
        for r in races:
            if r.id == race_id:
                return r
        return None

    def load_stations(self, station_id):
        base_key = f"station.{station_id}"
        id_ = self.cache[base_key + ".id"]
        if id_ is not None:
            name = self.cache[base_key + ".name"]
            if name is None:
                return None  # Invalid query
            services_joined = self.cache[base_key + ".services"]
            services = services_joined.split(";")
            system_id = self.cache[base_key + ".system_id"]
            type_id = self.cache[base_key + ".type_id"]
            race_id = self.cache[base_key + ".race_id"]
            s = Station(int(id_), name, services)
            s.system_id = system_id
            s.type_id = type_id
            s.race_id = race_id
            return s

        station = None
        try:
            station = self.api.load_stations(station_id)
        except RuntimeError:
            self.cache[base_key + ".id"] = station_id
            return None
        self.cache[base_key + ".id"] = station.id
        self.cache[base_key + ".name"] = station.name
        self.cache[base_key + ".services"] = ";".join(station.services)
        self.cache[base_key + ".race_id"] = station.race_id
        self.cache[base_key + ".type_id"] = station.type_id
        self.cache[base_key + ".system_id"] = station.system_id
        return station

    def load_structure(self, structure_id):
        base_key = f"structure.{structure_id}"
        id_ = self.cache[base_key + ".id"]
        if id_ is not None:
            name = self.cache[base_key + ".name"]
            if name is None:
                return None  # Invalid query
            system_id = self.cache[base_key + ".system_id"]
            type_id = self.cache[base_key + ".type_id"]
            owner_id = self.cache[base_key + ".owner_id"]
            return Structure(int(id_), name, system_id, type_id, owner_id)

        structure = None
        try:
            structure = self.api.load_structure(structure_id)
        except RuntimeError:
            self.cache[base_key + ".id"] = structure_id
            return None
        self.cache[base_key + ".id"] = structure.id
        self.cache[base_key + ".name"] = structure.name
        self.cache[base_key + ".system_id"] = structure.system_id
        self.cache[base_key + ".type_id"] = structure.type_id
        self.cache[base_key + ".owner_id"] = structure.owner_id
        return structure

    def load_type(self, type_id):
        base_key = f"type.{type_id}"
        id = self.cache[base_key + ".id"]
        if id is not None:
            name = self.cache[base_key + ".name"]
            description = self.cache[base_key + ".description"]
            volume = self.cache[base_key + ".volume"]
            packaged_volume = self.cache[base_key + ".packaged_volume"]
            group_id = self.cache[base_key + ".group_id"]
            t = Type(int(id), name, description, float(volume), float(packaged_volume))
            t.group_id = group_id
            return t

        type_ = self.api.load_type(type_id)
        self.cache[base_key + ".id"] = type_.id
        self.cache[base_key + ".name"] = type_.name
        self.cache[base_key + ".description"] = type_.description
        self.cache[base_key + ".volume"] = type_.volume
        self.cache[base_key + ".packaged_volume"] = type_.packaged_volume
        self.cache[base_key + ".group_id"] = type_.group_id
        return type_

    def load_group(self, group_id):
        base_key = f"group.{group_id}"
        id = self.cache[base_key + ".id"]
        if id is not None:
            name = self.cache[base_key + ".name"]
            category_id = self.cache[base_key + ".category_id"]
            g = Group(int(id), name)
            g.category_id = category_id
            return g

        group = self.api.load_group(group_id)
        self.cache[base_key + ".id"] = group.id
        self.cache[base_key + ".name"] = group.name
        self.cache[base_key + ".category_id"] = group.category_id
        return group

    def load_category(self, category_id):
        base_key = f"category.{category_id}"
        id = self.cache[base_key + ".id"]
        if id is not None:
            name = self.cache[base_key + ".name"]
            return Category(int(id), name)

        category = self.api.load_category(category_id)
        self.cache[base_key + ".id"] = category.id
        self.cache[base_key + ".name"] = category.name
        return category

    def load_all_groups_ids(self):
        return self.api.load_all_groups_ids()
