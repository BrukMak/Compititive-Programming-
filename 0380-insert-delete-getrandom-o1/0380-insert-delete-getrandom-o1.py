class RandomizedSet:

    def __init__(self):
        self.randomizedSet = defaultdict(int)
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        self.randomizedSet[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomizedSet:
            to_remove_index = self.randomizedSet[val]
            self.randomizedSet[self.values[-1]] = to_remove_index
            
            self.values[to_remove_index], self.values[-1] =  self.values[-1], self.values[to_remove_index]
            del self.randomizedSet[val]
            self.values.pop()
            return True
        return False
        

    def getRandom(self) -> int:       
        rand_index = randint(0, len(self.values)-1)
        return self.values[rand_index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()