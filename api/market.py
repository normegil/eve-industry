import requests

from cfg import eve_api


class MarketAPI:
    def __init__(self, tokens):
        self.tokens = tokens

    def load_character_order_history(self, character_id):
        resp = requests.get(eve_api.esi_base_address + "/characters/" + str(character_id) + "/orders/history",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        print(resp.content)
