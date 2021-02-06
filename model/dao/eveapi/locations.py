import json
import logging

import requests

from cfg import eve_api


class LocationAPI:
    def __init__(self, tokens):
        self.tokens = tokens

    def load_current_system_id(self, character_id):
        logging.info("Requesting current location")
        resp = requests.get(eve_api.esi_base_address + f"/characters/{character_id}/location/",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))
        content = json.loads(resp.content)
        return content["solar_system_id"]
