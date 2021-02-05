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
            costs.append(SystemCosts(indices["solar_system_id"], cost_indices["manufacturing"],
                                     cost_indices["researching_time_efficiency"],
                                     cost_indices["researching_material_efficiency"], cost_indices["copying"],
                                     cost_indices["invention"], cost_indices["reaction"]))
        return costs
