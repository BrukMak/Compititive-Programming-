class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        
        while l <= r:
            tempD = days
            cap = l + (r - l) // 2
            
            cur = cap
            for w in weights:
                if w > cur:
                    tempD -= 1
                    cur = cap
                cur -= w
                
            if tempD-1 >= 0:
                r = cap-1
            else:
                l = cap + 1
                
        return l