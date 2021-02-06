import json
import logging

import requests

from cfg import eve_api
from model.entities.industry import SystemCosts


class IndustryAPI:
    base_url = eve_api.esi_base_address + "/industry/"

    def __init__(self, tokens):
        self.tokens = tokens

    def load_cost_indices(self):
        logging.info(f"Requesting systems cost indices")
        resp = requests.get(self.base_url + "systems/",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)}")

        content = json.loads(resp.content)

        costs = []
        for indices in content:
            cost_indices = indices["cost_indices"]
            manufacturing = None
            researching_time_efficiency = None
            researching_material_efficiency = None
            copying = None
            invention = None
            reaction = None
            for i in cost_indices:
                key = i["activity"]
                value = i["cost_index"]
                if key == "manufacturing":
                    manufacturing = value
                elif key == "researching_time_efficiency":
                    researching_time_efficiency = value
                elif key == "researching_material_efficiency":
                    researching_material_efficiency = value
                elif key == "copying":
                    copying = value
                elif key == "invention":
                    invention = value
                elif key == "reaction":
                    reaction = value

            costs.append(SystemCosts(indices["solar_system_id"], manufacturing, researching_time_efficiency,
                                     researching_material_efficiency, copying, invention, reaction))
        return costs
