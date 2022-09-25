class FrontMiddleBackQueue:

    def __init__(self):
        self.que = []

    def pushFront(self, val: int) -> None:
        self.que.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        N = len(self.que)
        mid = N // 2
        self.que.insert(mid, val)
    def pushBack(self, val: int) -> None:
        self.que.append(val)
    def popFront(self) -> int:
        if len(self.que) > 0:
            return self.que.pop(0) if len(self.que) > 0 else -1
        return -1
    def popMiddle(self) -> int:
        if len(self.que) > 0:
            mid = len(self.que) // 2
            return self.que.pop(mid) if len(self.que) % 2 == 1 else self.que.pop(mid-1)
        return -1
    def popBack(self) -> int:
        return self.que.pop() if len(self.que) > 0 else -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()