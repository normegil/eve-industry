class SQLLiteDictAdapter:
    def __init__(self, sqllitedict):
        self.sqllitedict = sqllitedict

    def __getitem__(self, item):
        try:
            return self.sqllitedict[item]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self.sqllitedict[key] = value
