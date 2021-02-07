from datetime import datetime, timezone

from dateutil import parser


class DictAdapter:
    def __init__(self, sqllitedict):
        self.sqllitedict = sqllitedict

    def __getitem__(self, item):
        try:
            return self.sqllitedict[item]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self.sqllitedict[key] = value


class TimeoutCacheAdapter:
    def __init__(self, cache, timeout):
        self.cache = cache
        self.timeout = timeout

    def __getitem__(self, item):
        if not item.endswith(".id"):
            return self.cache[item]
        id_ = self.cache[item]
        if id_ is None:
            return None
        registered_time_str = self.cache[item + ".registered"]
        if registered_time_str is None:
            return None
        registered_time = parser.parse(registered_time_str)
        if datetime.now(timezone.utc) > registered_time + self.timeout:
            return None
        return id_

    def __setitem__(self, key, value):
        self.cache[key] = value
        if key.endswith(".id"):
            self.cache[key + ".registered"] = datetime.now(timezone.utc).isoformat()
