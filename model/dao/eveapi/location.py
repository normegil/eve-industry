from model.entities.assets import AssetLocation, AssetLocationStation, AssetLocationItem


def init_location(location_type, location_id):
    location = AssetLocation(location_type, location_id)
    if location_type == "station":
        location = AssetLocationStation(location_type, location_id)
    elif location_type == "item":
        location = AssetLocationItem(location_type, location_id)
    return location
