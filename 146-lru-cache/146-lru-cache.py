class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()
        self.itemsNumber = 0
    def get(self, key: int) -> int:
        if key in self.map:
            val = self.map.pop(key)
            self.map[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        else:
            if len(self.map) >= self.capacity:
                self.map.popitem(last = False)
        self.map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)