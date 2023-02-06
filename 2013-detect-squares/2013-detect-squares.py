class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pointList = []
    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.pointList.append(point)        

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for p1, p2 in self.pointList:
            if abs(p1 - x) != abs(p2 - y) or p1 == x or y == p2:
                continue
            ans += self.points[(x, p2)] * self.points[(p1, y)]
            
        # self.add(point)
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)