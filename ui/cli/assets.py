def report_assets(character, universe_dao, type_name=None, group_name=None):
    print(f"{character.name}:")
    for type_id, assets in character.assets.items():
        type_ = universe_dao.load_type(type_id)
        if group_name is None or group_name == type_.group.name:
            if type_name is None or type_name == type_.name:
                print(f"\tType: {type_.group.name}->{type_.name}:")
                print(f"\t\tQuantity owned: {assets.quantity}")
                print(f"\t\tAvg Price: {assets.average_price_per_unit()}")
                print(f"\t\tLocations:")
                for location in assets.by_locations:
                    if "station" != location.location_type:
                        print(f"\t\t\tLocation type unsupported: {location.location_type}")
                        continue

                    station = universe_dao.load_stations(location.location_id)
                    region_name = station.system.constellation.region.name
                    constellation_name = station.system.constellation.name
                    system_name = station.system.name
                    station_name = station.name
                    race = station.race.name
                    print(
                        f"\t\t\t{region_name} | {constellation_name} | {system_name} | {station_name} ({race}): {location.quantity}")
                for order in assets.buy_orders:
                    print(f"\t\tOrders:")
                    print(f"\t\t\t{order.id}:")
                    print(f"\t\t\t\tIssued: {order.issued}")
                    try:
                        station = universe_dao.load_stations(order.location_id)
                        print(
                            f"\t\t\t\tLocation: {station.system.constellation.region.name}->{station.system.name}->{station.name}")
                    except:
                        print(f"\t\t\t\tLocation: Unkown")
                    print(f"\t\t\t\tPrice: {order.price_per_unit}/unit")
                    print(f"\t\t\t\tState: {order.state}")
                    print(f"\t\t\t\tVolume: {order.volume_remain}/{order.volume_total}")
