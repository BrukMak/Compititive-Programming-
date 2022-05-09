class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timeDiff = 720
        for i in range(1, len(timePoints)):
            prev = timePoints[i-1]
            cur = timePoints[i]
            
            min_diff = int(int(cur[:2]) - int(prev[:2])) * 60
            min_diff += (int(cur[3:]) - int(prev[3:]))
            timeDiff = min(timeDiff, min_diff)
                         
        min_diff1 = int(24 - int(timePoints[-1][:2])) * 60
        min_diff1 += (0 - int(timePoints[-1][3:]))
        
        min_diff2 = int(timePoints[0][:2]) * 60
        min_diff2 += int(timePoints[0][3:])
         
        min_diff =  min_diff1 + min_diff2
        timeDiff = min(timeDiff, min_diff)
        
        return timeDiff
            