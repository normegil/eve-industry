from dateutil import parser

from model.entities.assets import Order


class MarketCache:
    def __init__(self, cache, api):
        self.__cache = cache
        self.api = api

    def load_character_order_history(self, character_id):
        return self.api.load_character_order_history(character_id)

    def load_orders(self, region_id, type_id):
        base_key = f"orders.{type_id}.{region_id}"
        order_ids = self.__cache[base_key + ".all.id"]
        if order_ids is not None:
            ids = order_ids.split(";")
            orders = []
            for id_ in ids:
                order_base_key = base_key + f".{id_}"
                issued_str = self.__cache[order_base_key + ".issued"]
                issued = parser.parse(issued_str)
                location_id = self.__cache[order_base_key + ".location_id"]
                price_per_unit = self.__cache[order_base_key + ".price_per_unit"]
                duration = self.__cache[order_base_key + ".duration"]
                type_id = self.__cache[order_base_key + ".type_id"]
                volume_remain = self.__cache[order_base_key + ".volume_remain"]
                volume_total = self.__cache[order_base_key + ".volume_total"]
                is_buy_order = self.__cache[order_base_key + ".is_buy_order"]
                orders.append(
                    Order(id_, issued, location_id, price_per_unit, duration, type_id, volume_remain, volume_total,
                          is_buy_order))
            return orders
        orders = self.api.load_orders(region_id, type_id)
        order_ids = []
        for order in orders:
            order_ids.append(order.id)
            order_base_key = base_key + f".{order.id}"
            self.__cache[order_base_key + ".issued"] = order.issued.isoformat()
            self.__cache[order_base_key + ".location_id"] = order.location.id
            self.__cache[order_base_key + ".price_per_unit"] = order.price_per_unit
            self.__cache[order_base_key + ".duration"] = order.duration
            self.__cache[order_base_key + ".type_id"] = order.type_id
            self.__cache[order_base_key + ".volume_remain"] = order.volume_remain
            self.__cache[order_base_key + ".volume_total"] = order.volume_total
            self.__cache[order_base_key + ".is_buy_order"] = order.is_buy_order
        self.__cache[base_key + ".all.id"] = ";".join(str(id_) for id_ in order_ids)
        return orders

    def load_prices(self):
        base_key = "prices"
        ids_str = self.__cache[base_key + ".all.id"]
        if ids_str is not None:
            ids = ids_str.split(";")
            prices = {}
            for id_ in ids:
                prices[id_] = self.__load_price(id_)
            return prices
        prices = self.api.load_prices()
        price_ids = []
        for id_ in prices:
            price_ids.append(id_)
            self.__save_price(id_, prices)
        self.__cache[base_key + ".all.id"] = ";".join(str(id_) for id_ in price_ids)
        return prices

    def load_price(self, type_id):
        base_key = f"prices.{type_id}"
        id_ = self.__cache[base_key + ".id"]
        if id_ is not None:
            return self.__load_price(id_)
        prices = self.load_prices()
        return prices[type_id]

    def __load_price(self, id_):
        price_base_key = f"prices.{id_}"
        adjusted_price = self.__cache[price_base_key + ".adjusted_price"]
        average_price = self.__cache[price_base_key + ".average_price"]
        return {
            "average_price": average_price,
            "adjusted_price": adjusted_price
        }

    def __save_price(self, id_, prices):
        price_base_key = f"prices.{id_}"
        self.__cache[price_base_key + ".id"] = id_
        self.__cache[price_base_key + ".adjusted_price"] = prices[id_]["adjusted_price"]
        if "average_price" in prices[id_]:
            self.__cache[price_base_key + ".average_price"] = prices[id_]["average_price"]
