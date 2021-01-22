class Model:
    def __init__(self, redis, tokens):
        self.redis = redis
        self.tokens = tokens