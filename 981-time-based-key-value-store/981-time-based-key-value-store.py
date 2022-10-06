class TimeMap:

    def __init__(self):
        self.mapy = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.mapy:
            self.mapy[key][timestamp] = value
        else:
            self.mapy[key] = {timestamp : value}

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mapy:
            return ''
        while (timestamp not in self.mapy[key]) and timestamp > 0:
            timestamp -= 1
        if timestamp == 0:
            return ''
        
        
        return self.mapy[key][timestamp]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)