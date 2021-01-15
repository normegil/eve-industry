from model import Race
from model.locations import Region, Constellation, Station, System
from model.types import Type, Group, Category


class UniverseCache:
    def __init__(self, conn, api):
        self.conn = conn
        self.api = api

    def load_region(self, region_id):
        base_key = f"region.{region_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            description = self.conn.get(base_key + ".description")
            return Region(int(id), name, description)

        region = self.api.load_region(region_id)
        self.conn.set(base_key + ".id", region.id)
        self.conn.set(base_key + ".name", region.name)
        self.conn.set(base_key + ".description", region.description)
        return region

    def load_constellation(self, constellation_id):
        base_key = f"constellation.{constellation_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            region_id = self.conn.get(base_key + ".region_id")
            c = Constellation(int(id), name)
            c.region_id = region_id
            return c

        constellation = self.api.load_constellation(constellation_id)
        self.conn.set(base_key + ".id", constellation.id)
        self.conn.set(base_key + ".name", constellation.name)
        self.conn.set(base_key + ".region_id", constellation.region_id)
        return constellation

    def load_system(self, system_id):
        base_key = f"system.{system_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            constellation_id = self.conn.get(base_key + ".constellation_id")
            s = System(int(id), name)
            s.constellation_id = constellation_id
            return s

        system = self.api.load_system(system_id)
        self.conn.set(base_key + ".id", system.id)
        self.conn.set(base_key + ".name", system.name)
        self.conn.set(base_key + ".constellation_id", system.constellation_id)
        return system

    def load_races(self):
        races = self.api.load_races()
        for race in races:
            self.conn.set(f"race.{race.id}.id", race.id)
            self.conn.set(f"race.{race.id}.name", race.name)
            self.conn.set(f"race.{race.id}.description", race.description)
        return races

    def load_race(self, race_id):
        id = self.conn.get(f"race.{race_id}.id")
        if id is not None:
            name = self.conn.get(f"race.{race_id}.name")
            description = self.conn.get(f"race.{race_id}.description")
            return Race(int(id), name, description)

        races = self.load_races()
        for r in races:
            if r.id == race_id:
                return r
        return None

    def load_stations(self, station_id):
        base_key = f"station.{station_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            services_joined = self.conn.get(base_key + ".services")
            services = services_joined.split(";")
            system_id = self.conn.get(base_key + ".system_id")
            type_id = self.conn.get(base_key + ".type_id")
            race_id = self.conn.get(base_key + ".race_id")
            s = Station(int(id), name, services)
            s.system_id = system_id
            s.type_id = type_id
            s.race_id = race_id
            return s

        station = self.api.load_stations(station_id)
        self.conn.set(base_key + ".id", station.id)
        self.conn.set(base_key + ".name", station.name)
        self.conn.set(base_key + ".services", ";".join(station.services))
        self.conn.set(base_key + ".race_id", station.race_id)
        self.conn.set(base_key + ".type_id", station.type_id)
        self.conn.set(base_key + ".system_id", station.system_id)
        return station

    def load_type(self, type_id):
        base_key = f"type.{type_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            description = self.conn.get(base_key + ".description")
            volume = self.conn.get(base_key + ".volume")
            packaged_volume = self.conn.get(base_key + ".packaged_volume")
            group_id = self.conn.get(base_key + ".group_id")
            t = Type(int(id), name, description, float(volume), float(packaged_volume))
            t.group_id = group_id
            return t

        type_ = self.api.load_type(type_id)
        self.conn.set(base_key + ".id", type_.id)
        self.conn.set(base_key + ".name", type_.name)
        self.conn.set(base_key + ".description", type_.description)
        self.conn.set(base_key + ".volume", type_.volume)
        self.conn.set(base_key + ".packaged_volume", type_.packaged_volume)
        self.conn.set(base_key + ".group_id", type_.group_id)
        return type_

    def load_group(self, group_id):
        base_key = f"group.{group_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            category_id = self.conn.get(base_key + ".category_id")
            g = Group(int(id), name)
            g.category_id = category_id
            return g

        group = self.api.load_group(group_id)
        self.conn.set(base_key + ".id", group.id)
        self.conn.set(base_key + ".name", group.name)
        self.conn.set(base_key + ".category_id", group.category_id)
        return group

    def load_category(self, category_id):
        base_key = f"category.{category_id}"
        id = self.conn.get(base_key + ".id")
        if id is not None:
            name = self.conn.get(base_key + ".name")
            return Category(int(id), name)

        category = self.api.load_category(category_id)
        self.conn.set(base_key + ".id", category.id)
        self.conn.set(base_key + ".name", category.name)
        return category
