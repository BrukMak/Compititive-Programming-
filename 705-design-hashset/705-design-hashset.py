class MyHashSet:

    def __init__(self):
        self.set_ = {}

    def add(self, key: int) -> None:
        if key not in self.set_:
            self.set_[key] = 0

    def remove(self, key: int) -> None:
        if key in self.set_:
            del self.set_[key]
        
    def contains(self, key: int) -> bool:
        
        return key in self.set_


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)