from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        minheap = []
        maxheap = []
        
        self.minheap = minheap
        self.maxheap = maxheap

    def addNum(self, num: int) -> None:
        if len (self.minheap) == 0:
            heappush(self.minheap, num)
        else:
            if num > self.minheap[0]:   
                heappush(self.minheap, num)
            else:
                heappush(self.maxheap, -num)
                
        while len(self.minheap) - len(self.maxheap) >= 2:
            heappush(self.maxheap, -heappop(self.minheap))
        while len(self.maxheap) - len(self.minheap) >= 2:
            heappush(self.minheap, -heappop(self.maxheap))
        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        else:
            return float((self.minheap[0] - self.maxheap[0]) / 2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
