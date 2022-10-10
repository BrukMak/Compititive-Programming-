class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        minEnd = intervals[0][1]
        count = 0
        for s, e in intervals[1:]:
            
            if s < minEnd:
                if e < minEnd:
                    minEnd = e
                count += 1
            else:
                minEnd = e
        return count