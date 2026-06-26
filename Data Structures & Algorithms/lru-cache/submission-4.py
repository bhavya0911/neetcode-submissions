class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = dict()
        self.used = list()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.used:
            self.used.remove(key)
        if key in self.cache:
            self.used.append(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if not (key in self.cache) and (len(self.cache) + 1) > self.cap:
            poper = self.used.pop(0)
            print(self.cache.pop(poper, None))

        self.cache[key] = value
        if key in self.used:
            self.used.remove(key)
        self.used.append(key)