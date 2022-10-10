class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        minEnd = points[0][1]
        count= len(points)
        for i in range(1, len(points)):
            s, e = points[i]
            if s <= minEnd:
                minEnd = min(minEnd, e)
                count  -= 1
            else:
                minEnd = e
        return count