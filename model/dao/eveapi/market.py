import json

import requests
from dateutil import parser

from cfg import eve_api
from model.entities.assets import Order


class MarketAPI:
    def __init__(self, tokens):
        self.tokens = tokens

    def load_character_order_history(self, character_id):
        resp = requests.get(eve_api.esi_base_address + "/characters/" + str(character_id) + "/orders/history",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        content = json.loads(resp.content)
        orders = []
        for order in content:
            issued_str = order["issued"]
            issued_ = parser.parse(issued_str)
            if "is_buy_order" in order:
                o = Order(order["order_id"], issued_, order["location_id"], order["price"], order["duration"],
                          order["type_id"], order["volume_remain"], order["volume_total"], order["is_buy_order"])
            else:
                o = Order(order["order_id"], issued_, order["location_id"], order["price"], order["duration"],
                          order["type_id"], order["volume_remain"], order["volume_total"])

            o.original = order
            orders.append(o)

        return orders
