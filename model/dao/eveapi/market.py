import json
import logging

import requests
from dateutil import parser

from cfg import eve_api
from model.entities.assets import Order


class MarketAPI:
    def __init__(self, tokens):
        self.tokens = tokens

    def load_character_order_history(self, character_id):
        logging.info(f"Requesting character orders history")
        resp = requests.get(eve_api.esi_base_address + "/characters/" + str(character_id) + "/orders/history",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        content = json.loads(resp.content)
        return self.__to_orders(content)

    def load_orders(self, region_id, type_id):
        logging.info(f"Requesting orders [Region:{region_id};Type:{type_id}]")
        orders = []
        status_code = None
        page = 1
        while status_code is None or status_code != 404:
            resp = requests.get(
                eve_api.esi_base_address + f"/markets/{region_id}/orders/?page={page}&type_id={type_id}",
                headers={'Authorization': F"Bearer {self.tokens.access_token}"})
            status_code = resp.status_code
            if resp.status_code == 404:
                continue
            if resp.status_code >= 300:
                raise RuntimeError("Wrong response code: " + str(resp.status_code))
            content = json.loads(resp.content)
            orders.extend(self.__to_orders(content))
            page += 1
        return orders

    def load_prices(self):
        logging.info(f"Requesting prices")
        resp = requests.get(eve_api.esi_base_address + "/markets/prices",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))
        content = json.loads(resp.content)
        prices_dict = {}
        for price in content:
            new_p = {}
            if "adjusted_price" in price:
                new_p["adjusted_price"] = price["adjusted_price"]
            if "average_price" in price:
                new_p["average_price"] = price["average_price"]
            prices_dict[price["type_id"]] = new_p
        return prices_dict

    def __to_orders(self, content_json):
        orders = []
        for order_json in content_json:
            o = self.__to_order(order_json)
            orders.append(o)
        return orders

    def __to_order(self, order_dict):
        issued_str = order_dict["issued"]
        issued_ = parser.parse(issued_str)
        if "is_buy_order" in order_dict:
            o = Order(order_dict["order_id"], issued_, order_dict["location_id"], order_dict["price"],
                      order_dict["duration"],
                      order_dict["type_id"], order_dict["volume_remain"], order_dict["volume_total"],
                      order_dict["is_buy_order"])
        else:
            o = Order(order_dict["order_id"], issued_, order_dict["location_id"], order_dict["price"],
                      order_dict["duration"],
                      order_dict["type_id"], order_dict["volume_remain"], order_dict["volume_total"])
        o.original = order_dict
        return o
