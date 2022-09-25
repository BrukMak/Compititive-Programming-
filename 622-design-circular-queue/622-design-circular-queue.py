class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.que = [None] * k
        self.f = 0
        self.r = 0
    def enQueue(self, value: int) -> bool:
        if self.que[self.r] == None:
            self.que[self.r] = value
            self.r = (self.r+1) % self.k    
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.que[self.f] = None
            self.f = (self.f+1) % self.k
            return True
        return False
            
    def Front(self) -> int:
        if not self.isEmpty():
            return self.que[self.f]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.que[(self.r + self.k - 1) % self.k]
        return -1

    def isEmpty(self) -> bool:
        
        if self.r == self.f and self.que[self.r] == None:
            return True
        return False
    def isFull(self) -> bool:
        if self.r == self.f and self.que[self.r] != None:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()