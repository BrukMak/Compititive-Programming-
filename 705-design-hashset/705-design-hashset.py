class MyHashSet:

    def __init__(self):
        self.set_ = []

    def add(self, key: int) -> None:
        if key not in self.set_:
            self.set_.append(key)

    def remove(self, key: int) -> None:
        if key in self.set_:
            self.set_.remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.set_:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)