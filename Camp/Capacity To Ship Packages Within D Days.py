class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isShipable(days, val):
            sum = 0
            for w in weights:
                sum += w
                if sum > val:
                    days -= 1
                    sum = w
                    if days == 0:
                        break
            return days > 0
        
        start = max(weights)
        end = sum(weights)
        
        while start <= end:
            mid = (start + end) // 2
            
            if not isShipable(days, mid):
                
                start = mid + 1
            else:
                end = mid - 1
                
        return start
