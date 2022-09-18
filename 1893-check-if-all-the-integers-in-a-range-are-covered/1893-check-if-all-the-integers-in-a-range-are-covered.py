class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for i in range(1, len(ranges)):
            if ranges[i-1][1] >= ranges[i][0]-1:
                ranges[i][0] = ranges[i-1][0]
                ranges[i][1] = max(ranges[i][1], ranges[i-1][1])
        for rg in ranges:
            if rg[0] <= left and rg[1] >= right:
                return True
        return False