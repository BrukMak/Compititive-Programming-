import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        left_right_height_pair = []
        # to identify which point is starting point or point on the left make the left negative
        for l, r, h in buildings:
            left_right_height_pair.append((l, -h))
            left_right_height_pair.append((r, h))
        
        #sort by starting point
        left_right_height_pair.sort()
        heights = sortedcontainers.SortedList([0])
        ans = []
        for r in left_right_height_pair:
            x, h = r
            
            # if start point add to the sortedList because its a possible candidate for
            # having max height on its range
            if h < 0:
                heights.add(-h)
            #if end point remove the height because its occurance is over
            else:
                heights.discard(h)
            
            # Check if there is a change in max height if so there if a new answer to be included

            if not ans or ans[-1][1] != heights[-1]:
                ans.append([x, heights[-1]])
        return ans