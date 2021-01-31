from .v0 import upgrade_to_v0
from .v1 import upgrade_to_v1

all_upgrades = [
    upgrade_to_v0,
    upgrade_to_v1
]


def upgrades(current_version):
    first_version_to_apply = current_version + 1
    if len(all_upgrades) <= first_version_to_apply:
        return []
    return all_upgrades[first_version_to_apply:]
