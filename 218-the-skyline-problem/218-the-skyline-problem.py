import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ranges = []
        # to identify which point is starting point or point on the left make the left negative
        for l, r, h in buildings:
            ranges.append((l, -h))
            ranges.append((r, h))
        
        #sort by starting point
        ranges.sort()
        heights = sortedcontainers.SortedList([0])
        ans = []
        for r in ranges:
            x, h = r
            
            # if start point add to the sortedList
            if h < 0:
                heights.add(-h)
            #if end point remove the point
            else:
                heights.discard(h)
            
            if not ans or ans[-1][1] != heights[-1]:
                ans.append([x, heights[-1]])
        return ans