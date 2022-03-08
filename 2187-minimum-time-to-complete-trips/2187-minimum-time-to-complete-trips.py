class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r =  totalTrips * min(time)
        best = 0
        while l <= r:
            
            mid = l + (r - l) // 2
            tempTot = 0
            
            for i in time:
                tempTot += mid // i
                
            if tempTot >= totalTrips:
                r = mid - 1
                best = mid
            elif tempTot < totalTrips:
                l = mid + 1
        
        return best
            