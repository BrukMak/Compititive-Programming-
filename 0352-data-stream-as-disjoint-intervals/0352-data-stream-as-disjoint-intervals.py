from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        self.sl = SortedList()

    def addNum(self, val: int) -> None:
        n = len(self.sl)
        i = self.sl.bisect_left([val, val])
        # val already added
        if i > 0 and self.sl[i-1][0] <= val <= self.sl[i-1][1] or i < n and self.sl[i][0] <= val <= self.sl[i][1]:
            pass
        # merge left & right
        elif 0 < i < n and self.sl[i-1][1] == val-1 and self.sl[i][0] == val+1:
            new = [self.sl[i-1][0], self.sl[i][1]]
            del self.sl[i]
            del self.sl[i-1]
            self.sl.add(new)
        # merge left only
        elif 0 < i and self.sl[i-1][1] == val-1:
            new = [self.sl[i-1][0], val]
            del self.sl[i-1]
            self.sl.add(new)
        # merge right only
        elif i < n and self.sl[i][0] == val+1:
            new = [val, self.sl[i][1]]
            del self.sl[i]
            self.sl.add(new)
        else:
            self.sl.add([val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.sl

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()